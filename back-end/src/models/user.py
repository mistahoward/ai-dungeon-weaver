from pydantic import EmailStr
from sqlalchemy import Integer, String, event
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from ..schemas import EpochTime, DatabaseOperation
class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[EmailStr] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    register_date: Mapped[EpochTime] = mapped_column(Integer)
    last_login_date: Mapped[EpochTime] = mapped_column(Integer)
    
    @staticmethod
    def after_insert(_, connection, target):
        from ..services import log_user_history
        log_user_history(target, connection, DatabaseOperation.CREATE)
    
    @staticmethod
    def after_update(_, connection, target):
        from ..services import log_user_history
        log_user_history(target, connection, DatabaseOperation.UPDATE)
        
    @staticmethod
    def after_delete(_, connection, target):
        from ..services import log_user_history
        log_user_history(target, connection, DatabaseOperation.DELETE)
        
event.listen(User, 'after_insert', User.after_insert)
event.listen(User, 'after_update', User.after_update)
event.listen(User, 'after_delete', User.after_delete)