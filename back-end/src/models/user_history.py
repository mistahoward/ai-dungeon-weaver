from base import Base
from user import User

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from schemas import EpochTime, DatabaseOperation
from sqlalchemy.orm import relationship
class UserHistory(Base):
	__tablename__ = "user_history"
	
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
	field_name: Mapped[str] = mapped_column(String)
	old_value: Mapped[str] = mapped_column(String)
	new_value: Mapped[str] = mapped_column(String)
	date: Mapped[EpochTime] = mapped_column(Integer)
	operation: Mapped[DatabaseOperation] = mapped_column(String)

	user: Mapped[User] = relationship("User", back_populates="user_history")