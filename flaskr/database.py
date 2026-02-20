from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def update_from_json(self, json):
        for field, value in json.model_dump(exclude_unset=True).items():
            setattr(self, field, value)


db = SQLAlchemy(model_class=Base)
