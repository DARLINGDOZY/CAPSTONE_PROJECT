from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import require_admin
from app.db.session import get_db
from app.schemas.course import CourseCreate, CourseResponse, CourseUpdate
from app.services.course_service import (
    create_course, delete_course, get_active_courses, get_course_by_id, update_course,
)

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=List[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    return get_active_courses(db)

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return get_course_by_id(db, course_id)

@router.post("/", response_model=CourseResponse, status_code=201)
def create(data: CourseCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    return create_course(db, data)

@router.put("/{course_id}", response_model=CourseResponse)
def update(course_id: int, data: CourseUpdate, db: Session = Depends(get_db), _=Depends(require_admin)):
    return update_course(db, course_id, data)

@router.delete("/{course_id}", status_code=204)
def delete(course_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    delete_course(db, course_id)