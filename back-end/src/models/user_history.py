from .base import Base
from .user import User
from schemas import EpochTime
from services import get_current_epoch_time

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.orm import relationship
class UserHistory(Base):
	__tablename__ = "user_history"
	
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
	field_name: Mapped[str] = mapped_column(String, nullable=True)
	old_value: Mapped[str] = mapped_column(String, nullable=True)
	new_value: Mapped[str] = mapped_column(String, nullable=True)
	timestamp: Mapped[EpochTime] = mapped_column(Integer, default=lambda: get_current_epoch_time())
	operation: Mapped[str] = mapped_column(String)

	user: Mapped[User] = relationship("User", back_populates="user_history")
 
	def to_dict(self):
		return {
			'id': self.id,
			'user_id': self.user_id,
			'field_name': self.field_name,
			'old_value': self.old_value,
			'new_value': self.new_value,
			'timestamp': self.timestamp,
			'operation': self.operation
		}