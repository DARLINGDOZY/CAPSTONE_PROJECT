from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import require_admin, require_student
from app.db.session import get_db
from app.schemas.enrollment import EnrollmentResponse, EnrollmentSimple
from app.services.enrollment_service import (
    admin_remove_student, deregister_student, enroll_student,
    get_all_enrollments, get_course_enrollments,
)

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.get("/", response_model=List[EnrollmentResponse])
def list_all_enrollments(db: Session = Depends(get_db), _=Depends(require_admin)):
    return get_all_enrollments(db)

@router.get("/course/{course_id}", response_model=List[EnrollmentResponse])
def list_course_enrollments(course_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    return get_course_enrollments(db, course_id)

@router.delete("/admin/{enrollment_id}", status_code=204)
def admin_remove(enrollment_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    admin_remove_student(db, enrollment_id)

@router.post("/{course_id}", response_model=EnrollmentSimple, status_code=201)
def enroll(course_id: int, db: Session = Depends(get_db), current_user=Depends(require_student)):
    return enroll_student(db, current_user, course_id)

@router.delete("/{course_id}", status_code=204)
def deregister(course_id: int, db: Session = Depends(get_db), current_user=Depends(require_student)):
    deregister_student(db, current_user, course_id)