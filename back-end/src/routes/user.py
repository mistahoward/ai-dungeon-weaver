from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..services import (
    get_db,
    user_exists,
    password_valid,
    create_new_user_in_database,
)
from ..schemas import UserResponse, UserCreateRequest

user_router = APIRouter()

@user_router.post("/user", response_model=UserResponse)
async def create_user(
    user_request: UserCreateRequest, db: Session = Depends(get_db)
) -> UserResponse:
    print("user_request: ", user_request)
    if user_exists(user_request, db):
        raise HTTPException(status_code=400, detail="User already exists")

    if not password_valid(user_request.password):
        raise HTTPException(
            status_code=400, detail="Password does not meet requirements"
        )

    try:
        created_user = create_new_user_in_database(user_request, db)
        return created_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
