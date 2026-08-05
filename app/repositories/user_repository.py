from app.core.security import hash_password, verify_password
from app.db.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session

from app.db.session import get_db

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email:str):
        return self.db.query(User).filter(User.email == email).first()
    def create_new_user(self , user_data: UserCreate , hashed_password: str ):
        db_user = User(full_name= user_data.full_name , password_hash=hashed_password, email= user_data.email )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def login_user(self, email:str , password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
             return None

        #check password
        if not verify_password(plain_password=password,hashed_password= user.password_hash):
          return None

        # if hash_password != user.password_hash:
        #     return None

        return user
