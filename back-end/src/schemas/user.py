from pydantic import BaseModel

class UserResponse(BaseModel):
	id: int
	name: str
	first_name: str
	last_name: str
	email: str
	register_date: int
	last_login_date: int