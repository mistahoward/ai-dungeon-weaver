from sqlalchemy.orm import Session

from models import User
from schemas import UserCreateRequest

def user_name_exists(name: str, db: Session) -> bool:
	""" Check if a user name exists in the database. """
	db_user = db.query(User).filter(User.name == name).first()
	if db_user:
		return True
	return False

def email_exists(email: str, db: Session) -> bool:
	""" Check if an email exists in the database. """
	db_user = db.query(User).filter(User.email == email).first()
	if db_user:
		return True
	return False

def format_name(name: str) -> str:
	""" Format a name to start case and remove extra spaces. """
	return name.strip().title()

def password_has_uppercase(password: str) -> bool:
	""" Check if a password has an uppercase character. """
	return any(char.isupper() for char in password)

def password_has_lowercase(password: str) -> bool:
	""" Check if a password has a lowercase character. """
	return any(char.islower() for char in password)

def password_has_number(password: str) -> bool:
	""" Check if a password has a number. """
	return any(char.isdigit() for char in password)

def password_has_special_character(password: str) -> bool:
	""" Check if a password has a special character. """
	return any(not char.isalnum() for char in password)

def password_valid(password: str) -> bool:
	"""
	Check if a password is valid.
	(One uppercase, one lowercase, one number, one special character, and at least 8 characters long)
	"""
	if len.password < 8:
		return False
	if not password_has_uppercase(password):
		return False
	if not password_has_lowercase(password):
		return False
	if not password_has_number(password):
		return False
	if not password_has_special_character(password):
		return False
	return True

def user_exists(user_to_check: UserCreateRequest) -> bool:
	""" Check if a user exists in the database.  """
	if user_name_exists(user_to_check.name):
		return True
	if email_exists(user_to_check.email):
		return True
	return False

def get_user_by_email(email: str, db: Session) -> User:
	""" Get a user by email. """
	return db.query(User).filter(User.email == email).first()

def get_user_by_name(name: str, db: Session) -> User:
	""" Get a user by name. """
	return db.query(User).filter(User.name == name).first()