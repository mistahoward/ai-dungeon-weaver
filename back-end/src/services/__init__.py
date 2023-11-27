from common import get_current_epoch_time, get_db, result_error_handler
from user import user_exists, password_valid
import os
from dotenv import load_dotenv
from auth import get_password_hash, verify_password, create_access_token, get_current_user, oauth2_scheme

from schemas import AuthSettings

load_dotenv()

__all__ = [
	"get_current_epoch_time",
	"get_db",
	"result_error_handler",
	"user_exists",
	"password_valid"
]

jwt_key = os.getenv("JWT_KEY")
jwt_alg = os.getenv("JWT_ALG")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

if not jwt_key:
	raise ValueError("JWT_KEY environment variable not set.")
if not jwt_alg:
	raise ValueError("JWT_ALG environment variable not set.")
if not access_token_expire_minutes:
	raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES environment variable not set.")

auth_settings = AuthSettings(
	secret_key=jwt_key,
	algorithm=jwt_alg,
	access_token_expire_minutes=access_token_expire_minutes
)

__all__ = [
	"get_current_epoch_time",
	"get_db",
	"result_error_handler",
	"user_exists",
	"password_valid",
	"auth_settings",
	"get_password_hash",
	"verify_password",
	"create_access_token",
	"get_current_user",
	"get_current_active_user",
	"oauth2_scheme"
]