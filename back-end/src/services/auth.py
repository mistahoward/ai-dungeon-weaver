from __future__ import annotations
from datetime import timedelta
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional, Union
import jwt
from passlib.context import CryptContext

from ..schemas import Token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """ Get a password hash for given password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ Verify a password. """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """ Create an access token. """
    from . import auth_settings
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, auth_settings.jwt_key, algorithm=auth_settings.jwt_alg)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """ Decode a given access token. """
    from . import auth_settings
    return jwt.decode(token, auth_settings.jwt_key, algorithms=[auth_settings.jwt_alg])

def handle_login(username: str, password: str, db: Session) -> Optional[Token]:
    # TODO: add logging to auth history table
    """ Handle login attempt. """
    from ..models import User
    from . import auth_settings
    from .user import get_user_by_name
    user: Optional[User] = get_user_by_name(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    access_token_expires = timedelta(minutes=auth_settings.access_token_expire_minutes)
    access_token = create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}