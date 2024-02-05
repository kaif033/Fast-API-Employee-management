from fastapi import FastAPI

from .database import engine
from . import models

from typing import List

from .routers import blog,user,login

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)

app.include_router(blog.router)


app.include_router(user.router)





 
