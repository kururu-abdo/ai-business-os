from app.core.security import hash_password
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from app.schemas.user import UserLogin, UserResponse ,UserCreate

class AuthService:
    def __init__(self,db:Session ):
        
        self.repo = UserRepository(db)

    def register_user(self, user_data: UserCreate):
        # Business logic: Check if email already exists
        existing_user = self.repo.get_user_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Fake hash for illustration (use passlib / bcrypt in production)
        hashed_password = hash_password(plain_password=user_data.password) 

        
        return self.repo.create_new_user(user_data, hashed_password)
    def login_user(self, login_data: UserLogin):
        return  self.repo.login_user(email=login_data.email, password=login_data.password)
    def get_user_profile(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user
    

