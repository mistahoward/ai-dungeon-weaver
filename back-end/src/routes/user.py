from fastapi import APIRouter, Depends
from schemas import UserResponse, UserCreateRequest
from sqlalchemy.orm import Session
from option import Result

from ..services import get_db, user_exists, password_valid, result_error_handler, create_new_user_in_database

router = APIRouter()

@router.post("/user")
@result_error_handler
async def create_user(user_request: UserCreateRequest, db: Session = Depends(get_db)) -> Result[UserResponse, str]:
    verify_unique_user = user_exists(user_request)
    if verify_unique_user is False: 
        return Result.Err("User already exists")
    verify_valid_password = password_valid(user_request.password)
    if verify_valid_password is False:
        return Result.Err("Password does not meet requirements")
    try:
        created_user = create_new_user_in_database(user_request, db)
        return Result.Ok(created_user)        
    except Exception as e:
        return Result.Err(str(e))