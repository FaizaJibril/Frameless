# frameless/app/db/models/image.py
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey,Boolean, Text
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    is_public = Column(Boolean, default=False)
    url = Column(String, nullable=False)
    description = Column(Text, nullable =True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id= Column(Integer,ForeignKey("users.id"))
    owner = relationship("User", back_populates="images")