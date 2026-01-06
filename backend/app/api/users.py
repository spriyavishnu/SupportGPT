from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.models.user import User
from app.core.permissions import require_roles
from app.core.roles import Role

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
async def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }



@router.get("/admin/users")
async def list_users(
    _: User = Depends(require_roles(Role.ADMIN))
):
    return {"message": "Only admins can see this"}