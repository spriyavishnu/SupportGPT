from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:

    async def register(self, db: AsyncSession, email: str, password: str):
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    async def authenticate(self, db: AsyncSession, email: str, password: str):
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalars().first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        token = create_access_token({
            "sub": str(user.id),
            "role": user.role
        })

        return token
