from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import create_refresh_token, hash_password, hash_token, verify_password, create_access_token
from app.models.refresh_token import RefreshToken

class AuthService:

    def register(self, db: Session, email: str, password: str):
        user = User(
            email=email,
            hashed_password=hash_password(password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    def authenticate(self, db: Session, email: str, password: str):
        result =  db.execute(select(User).where(User.email == email))
        user = result.scalars().first()

        if not user or not verify_password(password, user.hashed_password):
            return None

        token = create_access_token({
            "sub": str(user.id),
            "role": user.role
        })

        refresh_token = create_refresh_token()
        db_token = RefreshToken(
        user_id=user.id,
        token_hash=hash_token(refresh_token),
        expires_at=datetime.utcnow() + timedelta(days=7)
    )
        

        db.add(db_token)
        db.commit()


        return {
        "access_token": token,
        "refresh_token": refresh_token
    }
    

  

