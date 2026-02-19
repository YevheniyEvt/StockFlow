from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

__all__ = ('Base',)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)