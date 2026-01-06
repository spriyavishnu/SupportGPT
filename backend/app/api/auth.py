from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.services.auth_service import AuthService
from app.core.security import create_access_token, create_refresh_token, hash_token
from app.models.refresh_token import RefreshToken
from schemas.auth import RegisterRequest, LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])
auth_service = AuthService()

@router.get("/status")
def auth_status():
    return {"status": "Auth API is running", "endpoints": ["/register", "/login", "/refresh"]}

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return  auth_service.register(db, data.email, data.password)

@router.post("/login")
def login(data: LoginRequest, db:Session = Depends(get_db)):
    token =  auth_service.authenticate(db, data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}


@router.post("/refresh")
def refresh_token(
    token: str,
    db: Session = Depends(get_db)
):
    hashed = hash_token(token)

    result = db.execute(
        select(RefreshToken).where(RefreshToken.token_hash == hashed)
    )
    db_token = result.scalars().first()

    if not db_token or db_token.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    # ROTATION
    db.delete(db_token)

    new_access = create_access_token({
        "sub": str(db_token.user_id),
        "role": "user"
    })

    new_refresh = create_refresh_token()

    db.add(
        RefreshToken(
            user_id=db_token.user_id,
            token_hash=hash_token(new_refresh),
            expires_at=datetime.utcnow() + timedelta(days=7)
        )
    )

    db.commit()

    return {
        "access_token": new_access,
        "refresh_token": new_refresh
    }


