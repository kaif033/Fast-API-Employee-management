from fastapi import APIRouter, Depends,status,HTTPException,Response
from .. import schemas, models, database,oauth2
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(tags=["blogs"])

@router.get("/")
def return_hi():
    return f"hi i am checking my server"

@router.get("/blog", response_model=List[schemas.showblog])
def get_all(db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blogs = db.query(models.blog).all()
    return blogs


@router.post("/blog",status_code=status.HTTP_201_CREATED)
def blogs(request:schemas.blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    new_blog=models.blog(name=request.name,role=request.role,
                         salary=request.salary,company_name=request.company_name,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}',status_code=200,response_model=schemas.showblog)
def show_via_id(id,response:Response,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    blog=db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {id} not found in the database!!")
    return blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    """Deletes a blog with the given ID."""

    
    blog = db.query(models.blog).filter(models.blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")
    db.delete(blog)  
    db.commit()  
    return None  

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.blog, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    """Updates a blog with the given ID."""

    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")

    blog.name = request.name
    blog.role = request.role
    blog.salary = request.salary
    blog.company_name = request.company_name

    db.add(blog)
    db.commit()

    return "Blog updated successfully"
 