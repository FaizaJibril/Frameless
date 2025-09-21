"""Content schemas for API requests and responses."""
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class ContentBase(BaseModel):
    """Base content schema."""
    title: str = Field(..., min_length=1, max_length=200)
    theme: str = Field(..., min_length=1, max_length=100)
    is_story: bool = True
    is_public: bool = False


class ContentCreate(ContentBase):
    """Schema for creating content manually."""
    content: str = Field(..., min_length=1)
    image_url_1: str
    image_url_2: str
    image_url_3: str
    caption_1: str
    caption_2: str
    caption_3: str
    owner_id: int


class ContentGenerate(BaseModel):
    """Schema for AI content generation."""
    theme: str = Field(..., min_length=1, max_length=100)
    prompt: Optional[str] = Field(None, max_length=500)
    is_story: bool = True
    is_public: bool = False
    owner_id: int


class ContentUpdate(BaseModel):
    """Schema for updating content."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    theme: Optional[str] = Field(None, min_length=1, max_length=100)
    is_story: Optional[bool] = None
    is_public: Optional[bool] = None
    image_url_1: Optional[str] = None
    image_url_2: Optional[str] = None
    image_url_3: Optional[str] = None
    caption_1: Optional[str] = None
    caption_2: Optional[str] = None
    caption_3: Optional[str] = None


class ContentResponse(ContentBase):
    """Schema for content response."""
    id: int
    content: str
    image_url_1: str
    image_url_2: str
    image_url_3: str
    caption_1: str
    caption_2: str
    caption_3: str
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True
