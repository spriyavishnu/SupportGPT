from fastapi import Depends, HTTPException, status
from app.core.auth import get_current_user
from app.models.user import User

def require_roles(*allowed_roles: str):
    async def role_checker(user: User = Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission"
            )
        return user
    return role_checker
