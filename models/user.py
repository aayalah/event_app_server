from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
