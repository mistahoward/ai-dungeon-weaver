import time
from schemas import EpochTime

def get_current_epoch_time() -> EpochTime:
	return int(time.time())