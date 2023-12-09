import time
from sqlalchemy.orm import Session

from ..database import session_local
from ..schemas import EpochTime

def get_current_epoch_time() -> EpochTime:
	"""
	Get the current epoch time.
	Returns:
		EpochTime: The current epoch time.
	"""
	return int(time.time())

def get_db() -> Session:
	db = session_local()
	try:
		yield db
	finally:
		db.close()