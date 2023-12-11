from __future__ import annotations

from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from services import get_db, get_current_user
from models import User

auth_router = APIRouter()

@auth_router.post("/login", tags=["auth"])
async def login_for_access_token(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
    response: Response,
):
    """Login for access token."""
    from services import handle_login

    client_host = request.client.host if request.client is not None else "unknown"
    user_agent = request.headers.get("user-agent") or "unknown"

    token = handle_login(
        form_data.username, form_data.password, client_host, user_agent, db
    )
    if not token:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    response.set_cookie(key="access_token", value=token.access_token, httponly=True, secure=True, samesite="lax")
    return token.access_token
    # return { "success": True }

@auth_router.post("/token-test", tags=["auth"])
async def token_test(
    current_user: Annotated[User, Depends(get_current_user)]
):
	return current_user