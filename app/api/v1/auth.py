
from alembic.util import status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app import schemas
from app.core.auth import create_access_token, decode_access_token
from app.db.models.user import User
from app.schemas.user import UserLogin, UserResponse
from sqlalchemy.orm import Session
from app.models.enums import UserRole
from app.db.dependencies import get_db
from app.services.auth_service import AuthService
from fastapi import APIRouter, Depends, HTTPException, Response
from app.schemas.user import UserCreate
from app.api.dependencies.permissions import require_roles

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
router = APIRouter(prefix="/auth", tags=["Auth"])


def get_user_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    try:
        user_id = int(payload.get("sub"))
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


    
@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, service: AuthService = Depends(get_user_service)):
    return service.register_user(user_data)





@router.post("/login")
def login(login_data:UserLogin, service: AuthService = Depends(get_user_service)):
    user= service.login_user(login_data)
    if not user:
        
                 
                raise HTTPException(
                    status_code=401,
                    detail="Invalid credentials"
                )
    access_token = create_access_token(user_id=user.id , company_id=user.company_id , role=user.role )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id
    }

@router.get("/users/{user_id}")
def login(user_id: int, service: AuthService = Depends(get_user_service)):
     return service.get_user_profile(user_id=user_id)


@router.get("/me")
def get_me(current_user =Depends(require_roles(UserRole.ADMIN , UserRole.MANAGER, UserRole.EMPLOYEE,)),):
     return current_user

    
     