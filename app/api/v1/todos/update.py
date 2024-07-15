# app/api/v1/todos/update.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.todo import todo
from app.database.database import get_async_session
from app.schemas.todo import Todo, TodoUpdate

router = APIRouter()


@router.put('/{id}', response_model=Todo, summary='Atualizar o to-do pelo ID')
async def update_todo(
    *,
    db: AsyncSession = Depends(get_async_session),
    id: int,
    todo_in: TodoUpdate,
) -> Todo:
    """
    Update a Todo by ID.
    Args:
    - db (AsyncSession): AsyncSession dependency from get_db to interact with the database.
    - id (int): The ID of the Todo to update.
    - todo_in (TodoUpdate): Input data for updating the Todo.
    Returns:
    - Todo: The updated Todo object.
    Raises:
    - HTTPException 404: If the Todo with the given ID does not exist.
    """  # noqa: E501
    todo_item = await todo.get(db=db, id=id)
    if not todo_item:
        raise HTTPException(status_code=404, detail='To-do não encontrado')
    return await todo.update(db=db, db_obj=todo_item, obj_in=todo_in)
