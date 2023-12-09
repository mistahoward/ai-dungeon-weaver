from .base import Base
from ..schemas import EpochTime
from ..services import get_current_epoch_time

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AuthenticationLog(Base):
	__tablename__ = 'authentication_log'

	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
	timestamp: Mapped[EpochTime] = mapped_column(Integer, default=lambda: get_current_epoch_time())
	ip_address: Mapped[str] = mapped_column(String(15), nullable=False)
	user_agent: Mapped[str] = mapped_column(String(255), nullable=False)
	success: Mapped[bool] = mapped_column(Integer, nullable=False)
 
	user = relationship('User', back_populates='authentication_log')
 