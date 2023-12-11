import os
from dotenv import load_dotenv

from .common import get_current_epoch_time, get_db
from .user import user_exists, password_valid, create_new_user_in_database
from .auth import get_password_hash, verify_password, create_access_token, handle_login
from .user_history import log_user_history

from schemas import AuthSettings

load_dotenv()

__all__ = [
	"get_current_epoch_time",
	"get_db",
	"user_exists",
	"password_valid",
	"log_user_history",
	"create_new_user_in_database",
	"handle_login"
]


jwt_key = os.getenv("JWT_KEY")
jwt_alg = os.getenv("JWT_ALG")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or "30")

if not jwt_key:
	raise ValueError("JWT_KEY environment variable not set.")
if not jwt_alg:
	raise ValueError("JWT_ALG environment variable not set.")
if not access_token_expire_minutes:
	raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES environment variable not set.")

auth_settings = AuthSettings(
	jwt_key=jwt_key,
	jwt_alg=jwt_alg,
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
	# "get_current_user",
	"get_current_active_user",
	# "oauth2_scheme"
]