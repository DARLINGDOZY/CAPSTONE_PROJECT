from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm  # ✅ add this
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.schemas.token import Token
from app.schemas.user import UserRegister, UserResponse
from app.services.auth_service import authenticate_user, register_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, data)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):  # ✅ changed
    token = authenticate_user(db, form_data.username, form_data.password)  # ✅ .username not .email
    return Token(access_token=token)

@router.get("/me", response_model=UserResponse)
def get_profile(current_user=Depends(get_current_active_user)):
    return current_user