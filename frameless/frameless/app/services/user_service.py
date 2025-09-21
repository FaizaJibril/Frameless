"""User service for business logic."""
from typing import List, Optional
from sqlalchemy.orm import Session
from ..db.models.user import User
from ..schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """Service class for user operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    async def create_user(self, user: UserCreate) -> User:
        """Create a new user."""
        # Hash password
        hashed_password = pwd_context.hash(user.password)
        
        # Create user
        db_user = User(
            username=user.username,
            email=user.email,
            password=user.password,  # Store plain password for now
            hashed_password=hashed_password
        )
        
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()
    
    async def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.db.query(User).filter(User.username == username).first()
    
    async def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Get list of users."""
        return self.db.query(User).offset(skip).limit(limit).all()
    
    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """Update user information."""
        db_user = await self.get_user_by_id(user_id)
        if not db_user:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        
        # Hash password if provided
        if "password" in update_data:
            update_data["hashed_password"] = pwd_context.hash(update_data["password"])
        
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    async def delete_user(self, user_id: int) -> bool:
        """Delete user."""
        db_user = await self.get_user_by_id(user_id)
        if not db_user:
            return False
        
        self.db.delete(db_user)
        self.db.commit()
        return True
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password."""
        return pwd_context.verify(plain_password, hashed_password)
