from pydantic import BaseModel, EmailStr

from .common import EpochTime

class UserResponse(BaseModel):
	id: int
	name: str
	first_name: str
	last_name: str
	email: EmailStr
	register_date: EpochTime
	last_login_date: EpochTime

	def __init__(self, source_user):
		from models import User
		if not isinstance(source_user, User):
			raise TypeError("source_user must be a User instance")
		self.id = source_user.id
		self.name = source_user.name
		self.first_name = source_user.first_name
		self.last_name = source_user.last_name
		self.email = source_user.email
		self.register_date = source_user.register_date
		self.last_login_date = source_user.last_login_date

class UserCreateRequest(BaseModel):
	name: str
	first_name: str
	last_name: str
	email: str
	password: str
