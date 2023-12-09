from __future__ import annotations

from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from ..models import User

from ..schemas import DatabaseOperation
def log_user_history(user: User, db: Session, operation: DatabaseOperation) -> bool:
	""" Logs a user history event.

	Args:
		user (User): The "new" user object
		operation (DatabaseOperation): The type of operation

	Returns:
		bool: Boolean of success
	"""
	try:
		if operation == DatabaseOperation.UPDATE:
			inst = inspect(user)
			modified_attrs = [
				(attr.key, attr.history.deleted[0] if attr.history.deleted else None, attr.history.added[0] if attr.history.added else None)
				for attr in inst.attrs
				if attr.history.has_changes()
			]
			from ..models import UserHistory
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
			db.add_all(histories)
			db.commit()
			return True
		else:
			user_history = UserHistory(user_id=user.id, operation=operation)
			db.add(user_history)
			db.commit()
			return True
	except SQLAlchemyError as e:
		print(e)
		db.rollback()
		return False