# app/schemas/todo.py
from typing import Optional

from pydantic import BaseModel

from app.schemas.base_schemas import BaseSchema


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class Todo(BaseSchema, TodoBase):
    pass
