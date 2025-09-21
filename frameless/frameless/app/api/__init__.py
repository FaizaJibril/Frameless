"""The main APIRouter is defined to include all the sub routers from each
module inside the API folder"""
from fastapi import APIRouter
from .base import base_router
from .users import users_router
from .content import content_router
from .images import images_router
from .auth import auth_router

api_router = APIRouter()
api_router.include_router(base_router, tags=["base"])
api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(content_router, prefix="/content", tags=["content"])
api_router.include_router(images_router, prefix="/images", tags=["images"])
