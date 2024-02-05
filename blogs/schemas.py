from pydantic import BaseModel
from typing import List,Optional

class blog(BaseModel):
    name: str
    role: str
    salary: int
    company_name: str
    class Config:
        from_attributes = True

    
      # Updated for Pydantic V2
        
class User(BaseModel):
    username:str
    email:str
    password:str
    
class showuser(BaseModel):
    username: str
    email: str
    #blog:List[blog]
    class Config:
        from_attributes = True

        
class showblog(BaseModel):
    name:str
    role: str
    salary: int
    company_name: str
    creator:showuser
    class Config:
        from_attributes = True
        
class login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
