from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.schemas.token import Token
from app.schemas.user import UserLogin, UserRegister, UserResponse
from app.services.auth_service import authenticate_user, register_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, data)

@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, data.email, data.password)
    return Token(access_token=token)

@router.get("/me", response_model=UserResponse)
def get_profile(current_user=Depends(get_current_active_user)):
    return current_user