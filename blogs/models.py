from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class blog(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    salary=Column(Integer)
    company_name=Column(String)
    user_id=Column(Integer,ForeignKey('registrations.id'))
    creator=relationship("User",back_populates ="blog")
    
   
class User(Base):
    __tablename__ = "registrations"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email= Column(String)
    password=Column(Integer)
    
    
    
    blog=relationship("blog",back_populates ="creator")
    
