from pydantic import BaseModel

class AuthSettings (BaseModel):
	jwt_key: str
	jwt_alg: str
	access_token_expire_minutes: int
 
class Token (BaseModel):
	access_token: str
	token_type: str
