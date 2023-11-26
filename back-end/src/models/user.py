from base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from schemas import EpochTime
class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    salt: Mapped[str] = mapped_column(String)
    register_date: Mapped[EpochTime] = mapped_column(Integer)
    last_login_date: Mapped[EpochTime] = mapped_column(Integer)