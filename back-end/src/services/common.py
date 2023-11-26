import time
from schemas import EpochTime

def get_current_time() -> EpochTime:
	return int(time.time())
