"""Image management endpoints."""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..db.models.image import Image
from ..schemas.image import ImageResponse, ImageCreate
from ..services.image_service import ImageService

images_router = APIRouter()


@images_router.post("/images/upload", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
async def upload_image(
    file: UploadFile = File(...),
    description: str = None,
    is_public: bool = False,
    owner_id: int = None,
    db: Session = Depends(get_db)
) -> Any:
    """Upload a new image."""
    image_service = ImageService(db)
    return await image_service.upload_image(file, description, is_public, owner_id)


@images_router.post("/images", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
async def create_image(image: ImageCreate, db: Session = Depends(get_db)) -> Any:
    """Create image record with URL."""
    image_service = ImageService(db)
    return await image_service.create_image(image)


@images_router.get("/images/{image_id}", response_model=ImageResponse)
async def get_image(image_id: int, db: Session = Depends(get_db)) -> Any:
    """Get image by ID."""
    image_service = ImageService(db)
    image = await image_service.get_image_by_id(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image


@images_router.get("/images", response_model=List[ImageResponse])
async def list_images(
    skip: int = 0, 
    limit: int = 100, 
    is_public: bool = None,
    owner_id: int = None,
    db: Session = Depends(get_db)
) -> Any:
    """List images with optional filtering."""
    image_service = ImageService(db)
    return await image_service.get_images(
        skip=skip, 
        limit=limit, 
        is_public=is_public,
        owner_id=owner_id
    )


@images_router.delete("/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(image_id: int, db: Session = Depends(get_db)) -> Any:
    """Delete image."""
    image_service = ImageService(db)
    success = await image_service.delete_image(image_id)
    if not success:
        raise HTTPException(status_code=404, detail="Image not found")
