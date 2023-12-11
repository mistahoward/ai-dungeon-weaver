from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schemas import AuthAttempt

def log_auth_attempt(attempt: AuthAttempt, session: Session) -> bool:
	""" Logs an authentication attempt.

	Args:
		attempt (any): The authentication attempt
		session (Connection): The database session

	Returns:
		bool: Boolean of success
	"""
	from models import AuthenticationLog
	try:
		session.add(AuthenticationLog(
			user_id=attempt.user_id,
			user_agent=attempt.user_agent,
			ip_address=attempt.ip_address,
			success=attempt.success,
			timestamp=attempt.timestamp,
			failure_reason=attempt.failure_reason
		))

		return True
	except SQLAlchemyError as e:
		print("hit error block!")
		print(e)
		session.rollback()
		return False