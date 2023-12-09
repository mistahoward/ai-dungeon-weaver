from enum import Enum
from pydantic import BaseModel

from .common import EpochTime

class AuthSettings (BaseModel):
	jwt_key: str
	jwt_alg: str
	access_token_expire_minutes: int
 
class Token (BaseModel):
	access_token: str
	token_type: str

class FailureReason(Enum):
	""" Reasons for failed authentication. """
	BAD_PASSWORD = "Bad password"
	BAD_USERNAME = "Bad username"
	BAD_IP = "Bad IP"
	BAD_USER_AGENT = "Bad user agent"
	BAD_2FA = "Bad 2FA"

class AuthAttempt(BaseModel):
	user_id: int
	user_agent: str
	ip_address: str
	success: bool
	timestamp: EpochTime
	failure_reason: FailureReason = None