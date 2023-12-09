from sqlalchemy import Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from ..schemas import EpochTime, FailureReason
from ..services import get_current_epoch_time

class AuthenticationLog(Base):
	__tablename__ = 'authentication_log'

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
	timestamp: Mapped[EpochTime] = mapped_column(Integer, default=lambda: get_current_epoch_time())
	ip_address: Mapped[str] = mapped_column(String(15), nullable=False)
	user_agent: Mapped[str] = mapped_column(String(255), nullable=False)
	failure_reason: Mapped[FailureReason] = mapped_column(
        SQLEnum(FailureReason, values_callable=lambda obj: [e.value for e in obj]),
        nullable=True
    )
	success: Mapped[bool] = mapped_column(Integer, nullable=False)
 
	user = relationship('User', back_populates='authentication_log')
 