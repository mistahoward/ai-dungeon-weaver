from fastapi import APIRouter, Depends
from schemas import UserResponse, UserCreateRequest
from sqlalchemy.orm import Session

from services import get_db

router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreateRequest, db: Session = Depends(get_db)) -> UserResponse:
	return user
