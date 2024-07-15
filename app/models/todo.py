# app/models/todo.py
from sqlalchemy import Boolean, Column, Integer, String

from app.database.base_class import Base

from .base_model import BaseModelMixin


class Todo(BaseModelMixin, Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), index=True)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False)

    def __str__(self):
        return f'Todo #{self.id}: {self.title}, Completed: {self.is_completed}'
