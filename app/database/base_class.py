# app/database/base_class.py
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import DeclarativeMeta


class CustomBase:
    # Gerar o nome da tabela com base no nome da classe
    @declared_attr
    def __tablename__(cls):  # noqa: PLW3201
        return cls.__name__.lower()


Base: DeclarativeMeta = declarative_base(cls=CustomBase)
