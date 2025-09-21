from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username= Column(String,nullable =False, index =True, unique=True)
    email= Column(String,nullable =False, unique=True,index =True)
    password= Column(String,nullable =False, unique=True)
    hashed_password= Column(String,nullable =False)

# Relationships
    images = relationship("Image", back_populates="owner")
    generated_contents = relationship("GeneratedContent", back_populates="owner")