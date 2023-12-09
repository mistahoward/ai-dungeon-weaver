from sqlalchemy import Connection
from sqlalchemy.exc import SQLAlchemyError

from ..schemas import AuthAttempt

def log_auth_attempt(attempt: AuthAttempt, connection: Connection) -> bool:
	""" Logs an authentication attempt.

	Args:
		attempt (any): The authentication attempt
		connection (Connection): The database connection

	Returns:
		bool: Boolean of success
	"""
	from ..models import AuthenticationLog
	try:
		connection.execute(AuthenticationLog.__table__.insert().values({
			'user_id': attempt.user_id,
			'user_agent': attempt.user_agent,
			'ip_address': attempt.ip_address,
			'success': attempt.success,
			'timestamp': attempt.timestamp,
			'failure_reason': attempt.failure_reason
		}))

		return True
	except SQLAlchemyError as e:
		print("hit error block!")
		print(e)
		connection.rollback()
		return False