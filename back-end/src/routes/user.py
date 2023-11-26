from fastapi import APIRouter
from schemas import UserResponse, UserCreateRequest

router = APIRouter()

@router.post("/user", response_model=UserResponse)
async def create_user(user: UserCreateRequest) -> UserResponse:
	return user
