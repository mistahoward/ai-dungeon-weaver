from datetime import timedelta
import datetime
from typing import Union
import jwt
from passlib.context import CryptContext

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
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, auth_settings.jwt_key, algorithm=auth_settings.jwt_alg)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """ Decode a given access token. """
    from . import auth_settings
    return jwt.decode(token, auth_settings.jwt_key, algorithms=[auth_settings.jwt_alg])
