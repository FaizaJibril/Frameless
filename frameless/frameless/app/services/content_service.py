"""Content service for business logic."""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..db.models.contents import GeneratedContent
from ..schemas.content import ContentCreate, ContentUpdate, ContentGenerate
import requests
import os
import uuid


class ContentService:
    """Service class for content operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def create_content(self, content: ContentCreate) -> GeneratedContent:
        """Create content manually."""
        db_content = GeneratedContent(
            title=content.title,
            content=content.content,
            theme=content.theme,
            is_story=content.is_story,
            is_public=content.is_public,
            image_url_1=content.image_url_1,
            image_url_2=content.image_url_2,
            image_url_3=content.image_url_3,
            caption_1=content.caption_1,
            caption_2=content.caption_2,
            caption_3=content.caption_3,
            owner_id=content.owner_id
        )
        
        self.db.add(db_content)
        self.db.commit()
        self.db.refresh(db_content)
        return db_content
    
    async def generate_content(self, content_request: ContentGenerate) -> GeneratedContent:
        """Generate content using AI."""
        # Generate content using OpenAI API (placeholder implementation)
        generated_content = await self._call_openai_api(content_request)
        
        db_content = GeneratedContent(
            title=generated_content["title"],
            content=generated_content["content"],
            theme=content_request.theme,
            is_story=content_request.is_story,
            is_public=content_request.is_public,
            image_url_1=generated_content["image_url_1"],
            image_url_2=generated_content["image_url_2"],
            image_url_3=generated_content["image_url_3"],
            caption_1=generated_content["caption_1"],
            caption_2=generated_content["caption_2"],
            caption_3=generated_content["caption_3"],
            owner_id=content_request.owner_id
        )
        
        self.db.add(db_content)
        self.db.commit()
        self.db.refresh(db_content)
        return db_content
    
    async def get_content_by_id(self, content_id: int) -> Optional[GeneratedContent]:
        """Get content by ID."""
        return self.db.query(GeneratedContent).filter(GeneratedContent.id == content_id).first()
    
    async def get_content(self, skip: int = 0, limit: int = 100, theme: str = None, is_public: bool = None) -> List[GeneratedContent]:
        """Get list of content with optional filtering."""
        query = self.db.query(GeneratedContent)
        
        if theme:
            query = query.filter(GeneratedContent.theme == theme)
        if is_public is not None:
            query = query.filter(GeneratedContent.is_public == is_public)
        
        return query.offset(skip).limit(limit).all()
    
    async def update_content(self, content_id: int, content_update: ContentUpdate) -> Optional[GeneratedContent]:
        """Update content."""
        db_content = await self.get_content_by_id(content_id)
        if not db_content:
            return None
        
        update_data = content_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_content, field, value)
        
        self.db.commit()
        self.db.refresh(db_content)
        return db_content
    
    async def delete_content(self, content_id: int) -> bool:
        """Delete content."""
        db_content = await self.get_content_by_id(content_id)
        if not db_content:
            return False
        
        self.db.delete(db_content)
        self.db.commit()
        return True
    
    async def _call_openai_api(self, content_request: ContentGenerate) -> dict:
        """Call OpenAI API to generate content (placeholder implementation)."""
        # This is a placeholder - you would integrate with actual OpenAI API
        # For now, return mock data
        
        prompt = content_request.prompt or f"Create a {content_request.theme} story"
        
        return {
            "title": f"Generated {content_request.theme} Story",
            "content": f"This is a generated story about {content_request.theme}. {prompt}",
            "image_url_1": "https://via.placeholder.com/300x200?text=Image+1",
            "image_url_2": "https://via.placeholder.com/300x200?text=Image+2", 
            "image_url_3": "https://via.placeholder.com/300x200?text=Image+3",
            "caption_1": f"Caption for {content_request.theme} image 1",
            "caption_2": f"Caption for {content_request.theme} image 2",
            "caption_3": f"Caption for {content_request.theme} image 3"
        }
