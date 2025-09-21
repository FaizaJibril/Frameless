"""Image service for business logic."""
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import UploadFile
from ..db.models.image import Image
from ..schemas.image import ImageCreate
import os
import uuid
import aiofiles


class ImageService:
    """Service class for image operations."""
    
    def __init__(self, db: Session):
        self.db = db
        self.upload_dir = "uploads/images"
        os.makedirs(self.upload_dir, exist_ok=True)
    
    async def upload_image(self, file: UploadFile, description: str = None, is_public: bool = False, owner_id: int = None) -> Image:
        """Upload and save image file."""
        # Generate unique filename
        file_extension = file.filename.split(".")[-1] if "." in file.filename else "jpg"
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = os.path.join(self.upload_dir, unique_filename)
        
        # Save file
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Create image record
        image_url = f"/uploads/images/{unique_filename}"
        db_image = Image(
            url=image_url,
            description=description,
            is_public=is_public,
            owner_id=owner_id
        )
        
        self.db.add(db_image)
        self.db.commit()
        self.db.refresh(db_image)
        return db_image
    
    async def create_image(self, image: ImageCreate) -> Image:
        """Create image record with URL."""
        db_image = Image(
            url=image.url,
            description=image.description,
            is_public=image.is_public,
            owner_id=image.owner_id
        )
        
        self.db.add(db_image)
        self.db.commit()
        self.db.refresh(db_image)
        return db_image
    
    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        """Get image by ID."""
        return self.db.query(Image).filter(Image.id == image_id).first()
    
    async def get_images(self, skip: int = 0, limit: int = 100, is_public: bool = None, owner_id: int = None) -> List[Image]:
        """Get list of images with optional filtering."""
        query = self.db.query(Image)
        
        if is_public is not None:
            query = query.filter(Image.is_public == is_public)
        if owner_id is not None:
            query = query.filter(Image.owner_id == owner_id)
        
        return query.offset(skip).limit(limit).all()
    
    async def delete_image(self, image_id: int) -> bool:
        """Delete image."""
        db_image = await self.get_image_by_id(image_id)
        if not db_image:
            return False
        
        # Delete file if it exists locally
        if db_image.url.startswith("/uploads/"):
            file_path = db_image.url[1:]  # Remove leading slash
            if os.path.exists(file_path):
                os.remove(file_path)
        
        self.db.delete(db_image)
        self.db.commit()
        return True
