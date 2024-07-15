# app/api/v1/todos/delete.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.todo import todo
from app.database.database import get_async_session
from app.schemas.todo import Todo

router = APIRouter()


@router.delete(
    '/{id}', response_model=Todo, summary='Deletar um to-do pelo ID'
)  # noqa: E501
async def delete_todo(
    *, db: AsyncSession = Depends(get_async_session), id: int
) -> Todo:
    """
    Delete a Todo by ID.
    Args:
    - db (AsyncSession): AsyncSession dependency from get_db to interact with the database.
    - id (int): The ID of the Todo to delete.
    Returns:
    - Todo: The deleted Todo object.
    Raises:
    - HTTPException 404: If the Todo with the given ID does not exist.
    """  # noqa: E501
    todo_item = await todo.get(db=db, id=id)
    if not todo_item:
        raise HTTPException(status_code=404, detail='To-do não encontrado')
    return await todo.remove(db=db, id=id)
