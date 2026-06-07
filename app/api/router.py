from fastapi import APIRouter
from app.api.endpoints import auth, courses, enrollments

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(courses.router)
api_router.include_router(enrollments.router)