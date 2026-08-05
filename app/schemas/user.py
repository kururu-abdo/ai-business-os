from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
# Shared properties across all user schemas
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True

    class Config:
        from_attributes = True

class UserCreate(UserBase):
        full_name : str
        company_id: Optional[int] = None
        email: str
        password: str
        role: Optional[str] = None




# Data returned to the client (excludes sensitive info like passwords)
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
class UserLogin(UserBase):
     email: str 
     password: str