from sqlalchemy.orm import Mapped, mapped_column

from simple_project.models.base import Base


class Product(Base):
    __tablename__ = "products"
    name: Mapped[str]
    # Keep the existing SQLite column name so current data remains readable.
    description: Mapped[str] = mapped_column("desciption")
    price: Mapped[int]
