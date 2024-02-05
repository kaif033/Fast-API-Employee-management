from fastapi import APIRouter, Depends,status,HTTPException,Response
from .. import schemas, models, database,hashing
from sqlalchemy.orm import Session
from typing import List


get_db=database.get_db

router=APIRouter(tags=["Users"])

@router.post('/user',response_model=schemas.showuser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(username=request.username,email=request.email,
                         password=hashing.hash.brypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}",response_model=schemas.showuser)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {id} not found in the database!!")
    return user
    

