"""User management endpoints."""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..db.models.user import User
from ..schemas.user import UserCreate, UserResponse, UserUpdate
from ..services.user_service import UserService

users_router = APIRouter()


@users_router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> Any:
    """Create a new user."""
    user_service = UserService(db)
    return await user_service.create_user(user)


@users_router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    """Get user by ID."""
    user_service = UserService(db)
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.get("/users", response_model=List[UserResponse])
async def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    """List all users."""
    user_service = UserService(db)
    return await user_service.get_users(skip=skip, limit=limit)


@users_router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)) -> Any:
    """Update user information."""
    user_service = UserService(db)
    user = await user_service.update_user(user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    """Delete a user."""
    user_service = UserService(db)
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
