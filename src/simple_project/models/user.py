from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from simple_project.models.base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
