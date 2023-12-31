from __future__ import annotations

from sqlalchemy import Connection, insert, inspect
from sqlalchemy.exc import SQLAlchemyError

from models import User
from schemas import DatabaseOperation

def log_user_history(user: User, connection: Connection, operation: DatabaseOperation) -> bool:
	""" Logs a user history event.

	Args:
		user (User): The "new" user object
		operation (DatabaseOperation): The type of operation

	Returns:
		bool: Boolean of success
	"""
	from models import UserHistory
	try:
		if operation == DatabaseOperation.UPDATE:
			inst = inspect(user)
			modified_attrs = [
				(attr.key, attr.history.deleted[0] if attr.history.deleted else None, attr.history.added[0] if attr.history.added else None)
				for attr in inst.attrs
				if attr.history.has_changes()
			]
			histories = [
				UserHistory(
					user_id=user.id,
					field_name=field, 
					old_value=str(old),
					new_value=str(new),
					operation=operation
				)
				for field, old, new in modified_attrs
			]
			histories_dict = [history.to_dict() for history in histories]
			connection.execute(insert(UserHistory), histories_dict)
			return True
		else:
			user_history = UserHistory(user_id=user.id, operation=operation)
			connection.execute(insert(UserHistory), user_history.to_dict())

			return True
	except SQLAlchemyError as e:
		print("hit error block!")
		print(e)
		connection.rollback()
		return False