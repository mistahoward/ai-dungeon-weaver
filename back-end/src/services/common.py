import time
from typing import Generator
from sqlalchemy.orm import Session

from database import session_local
from schemas import EpochTime

def get_current_epoch_time() -> EpochTime:
	"""
	Get the current epoch time.
	Returns:
		EpochTime: The current epoch time.
	"""
	return EpochTime(int(time.time()))

def get_db() -> Generator[Session, None, None]:
	db = session_local()
	try:
		yield db
	finally:
		db.close()