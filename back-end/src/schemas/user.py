from pydantic import BaseModel, EmailStr

from common import EpochTime
class UserResponse(BaseModel):
	id: int
	name: str
	first_name: str
	last_name: str
	email: EmailStr
	register_date: EpochTime
	last_login_date: EpochTime
 
class UserCreateRequest(BaseModel):
	name: str
	first_name: str
	last_name: str
	email: str
	password: str
