"""Content management endpoints."""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..db.models.contents import GeneratedContent
from ..schemas.content import ContentCreate, ContentResponse, ContentUpdate, ContentGenerate
from ..services.content_service import ContentService

content_router = APIRouter()


@content_router.post("/content/generate", response_model=ContentResponse, status_code=status.HTTP_201_CREATED)
async def generate_content(content_request: ContentGenerate, db: Session = Depends(get_db)) -> Any:
    """Generate new content using AI."""
    content_service = ContentService(db)
    return await content_service.generate_content(content_request)


@content_router.post("/content", response_model=ContentResponse, status_code=status.HTTP_201_CREATED)
async def create_content(content: ContentCreate, db: Session = Depends(get_db)) -> Any:
    """Create new content manually."""
    content_service = ContentService(db)
    return await content_service.create_content(content)


@content_router.get("/content/{content_id}", response_model=ContentResponse)
async def get_content(content_id: int, db: Session = Depends(get_db)) -> Any:
    """Get content by ID."""
    content_service = ContentService(db)
    content = await content_service.get_content_by_id(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content


@content_router.get("/content", response_model=List[ContentResponse])
async def list_content(
    skip: int = 0, 
    limit: int = 100, 
    theme: str = None,
    is_public: bool = None,
    db: Session = Depends(get_db)
) -> Any:
    """List content with optional filtering."""
    content_service = ContentService(db)
    return await content_service.get_content(
        skip=skip, 
        limit=limit, 
        theme=theme, 
        is_public=is_public
    )


@content_router.put("/content/{content_id}", response_model=ContentResponse)
async def update_content(content_id: int, content_update: ContentUpdate, db: Session = Depends(get_db)) -> Any:
    """Update content."""
    content_service = ContentService(db)
    content = await content_service.update_content(content_id, content_update)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content


@content_router.delete("/content/{content_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_content(content_id: int, db: Session = Depends(get_db)) -> Any:
    """Delete content."""
    content_service = ContentService(db)
    success = await content_service.delete_content(content_id)
    if not success:
        raise HTTPException(status_code=404, detail="Content not found")
