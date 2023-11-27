from pydantic import BaseModel

class AuthSettings (BaseModel):
	def __init__(self, jwt_key: str, jwt_alg: str, access_token_expire_minutes: int):
		self.jwt_key = jwt_key
		self.jwt_alg = jwt_alg
		self.access_token_expire_minutes = access_token_expire_minutes

class Token (BaseModel):
	access_token: str
	token_type: str