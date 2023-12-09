from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..schemas import Token
from ..services import get_db

auth_router = APIRouter()

@auth_router.post("/login", response_model=Token, tags=["auth"])
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	""" Login for access token. """
	from ..services import handle_login
	client_host = request.client.host
	user_agent = request.headers.get('user-agent')
	
	token = handle_login(form_data.username, form_data.password, client_host, user_agent, db)
	if not token:
		raise HTTPException(status_code=401, detail="Incorrect username or password")
	return token