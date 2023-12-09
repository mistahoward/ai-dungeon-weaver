from typing import NewType

EpochTime = NewType('EpochTime', int)

class DatabaseOperation(str):
	INSERT = "INSERT"
	UPDATE = "UPDATE"
	DELETE = "DELETE"