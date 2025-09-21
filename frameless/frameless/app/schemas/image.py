"""Image schemas for API requests and responses."""
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ImageBase(BaseModel):
    """Base image schema."""
    url: str
    description: Optional[str] = None
    is_public: bool = False


class ImageCreate(ImageBase):
    """Schema for creating image record."""
    owner_id: int


class ImageResponse(ImageBase):
    """Schema for image response."""
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True
