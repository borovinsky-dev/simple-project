from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


# Базовый класс необходимый для создания сущностей в базе данных
# __abstract__ говорит о том, что таблица Base не должна создаваться, а поле id-
# вынесено, так как у всех производных классов, у остальных сущностей будет это поле
class Base(DeclarativeBase):
    __abstract__ = True

    # использует наименование класса, чтобы не писать __tablename__
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
