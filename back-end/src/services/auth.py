from __future__ import annotations
from datetime import timedelta
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Annotated, Optional, Union
import jwt
from passlib.context import CryptContext

from .user import get_user_by_name
from .authentication_log import log_auth_attempt
from schemas import Token, AuthAttempt, FailureReason
from .common import get_current_epoch_time, get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Get a password hash for given password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(
    data: dict, expires_delta: Union[timedelta, None] = None
) -> str:
    """Create an access token."""
    from . import auth_settings

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, auth_settings.jwt_key, algorithm=auth_settings.jwt_alg
    )
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """Decode a given access token."""
    from . import auth_settings

    return jwt.decode(token, auth_settings.jwt_key, algorithms=[auth_settings.jwt_alg])

def validate_access_token(token: str) -> bool:
    """Validate a given access token."""
    decoded_token = decode_access_token(token)
    if not decoded_token:
        return False
    if "exp" not in decoded_token:
        return False
    if decoded_token["exp"] < get_current_epoch_time():
        return False
    return True

def handle_login(username: str, password: str, ip: str, user_agent: str, db: Session) -> Optional[Token]:
    # TODO: add logging to auth history table
    """Handle login attempt."""
    from . import auth_settings
    from models import User

    user: Optional[User] = get_user_by_name(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        attempt = AuthAttempt(
            user_id=user.id,
            user_agent=user_agent,
            ip_address=ip,
            success=False,
            timestamp=get_current_epoch_time(),
            failure_reason=FailureReason.BAD_PASSWORD
        )
        log_auth_attempt(attempt, db)
        return None
    access_token_expires = timedelta(minutes=auth_settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

token_auth_scheme = HTTPBearer()

async def get_current_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(token_auth_scheme)]): 
    """Get current access token from request."""
    return credentials.credentials

async def get_current_user(token: str = Depends(get_current_token), db: Session = Depends(get_db)):
    """Get current user from request."""
    from models import User

    if not validate_access_token(token):
        return None
    decoded_token = decode_access_token(token)
    if not decoded_token:
        return None
    if "sub" not in decoded_token:
        return None
    user: Optional[User] = get_user_by_name(decoded_token["sub"], db)
    print(user)
    return user