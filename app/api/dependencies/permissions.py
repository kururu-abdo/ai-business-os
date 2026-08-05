from fastapi import Depends, HTTPException, status

from app.api.dependencies.auth import get_current_user
from app.models.enums import UserRole
from app.db.models.user import User


def require_roles(*roles: UserRole):
    def checker(
        current_user: User = Depends(get_current_user),
    ):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action.",
            )
        return current_user

    return checker