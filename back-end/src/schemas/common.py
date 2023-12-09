from enum import Enum
from typing import NewType

EpochTime = NewType('EpochTime', int)

class DatabaseOperation(Enum):
	INSERT = "INSERT"
	UPDATE = "UPDATE"
	DELETE = "DELETE"