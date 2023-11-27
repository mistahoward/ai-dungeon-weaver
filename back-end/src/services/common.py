from functools import wraps
from fastapi import HTTPException
from option import Result
import time
from sqlalchemy.orm import Session

from database import session_local
from schemas import EpochTime

def result_error_handler(endpoint_func):
    """ Decorator to handle Result errors. """
    @wraps(endpoint_func)
    async def wrapper(*args, **kwargs):
        result = await endpoint_func(*args, **kwargs)
        if isinstance(result, Result) and result.is_err():
            raise HTTPException(status_code=400, detail=result.unwrap_err())
        return result
    return wrapper

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