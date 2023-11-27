def user_name_exists(name: str) -> bool:
	"""Check if a user name exists in the database."""
	return True

def email_exists(email: str) -> bool:
	"""Check if an email exists in the database."""
	return True

def format_name(name: str) -> str:
	"""
	Format a name to start case and remove extra spaces.
	"""
	return name.strip().title()


def password_has_uppercase(password: str) -> bool:
	"""
	Check if a password has an uppercase character.
	"""
	return any(char.isupper() for char in password)


def password_has_lowercase(password: str) -> bool:
	"""
	Check if a password has a lowercase character.
	"""
	return any(char.islower() for char in password)

def password_has_number(password: str) -> bool:
	"""
	Check if a password has a number.
	"""
	return any(char.isdigit() for char in password)

def password_has_special_character(password: str) -> bool:
	"""
	Check if a password has a special character.
	"""
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
