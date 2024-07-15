# app/api/v1/todos/read.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.todo import todo
from app.database.database import get_async_session
from app.schemas.todo import Todo

router = APIRouter()


@router.get(
    '/', response_model=List[Todo] or None, summary='Obter todos os to-dos'
)
async def read_todos(
    *,
    db: AsyncSession = Depends(get_async_session),
    skip: int = 0,
    limit: int = 100,
) -> List[Todo]:
    """
    Recupera todos os Todos.
    Args:
    - db (AsyncSession): Dependência AsyncSession de get_db para interagir com o banco de dados.
    - skip (int): Número de registros a serem ignorados (padrão é 0).
    - limit (int): Número máximo de registros a serem retornados (padrão é 100).
    Returns:
    - List[Todo]: Uma lista de objetos Todo recuperados.
    Raises:
    - HTTPException 404: Se nenhum Todo for encontrado.
    """  # noqa: E501
    todos = await todo.get_multi(db=db, skip=skip, limit=limit)
    return todos


@router.get('/{id}', response_model=Todo, summary='Obter um to-do pelo ID')
async def read_todo(
    *, db: AsyncSession = Depends(get_async_session), id: int
) -> Todo:
    """
    Obtém um Todo pelo ID.
    Args:
    - db (AsyncSession): Dependência AsyncSession de get_db para interagir com o banco de dados.
    - id (int): O ID do Todo a ser recuperado.
    Returns:
    - Todo: O objeto Todo recuperado.
    Raises:
    - HTTPException 404: Se o Todo com o ID fornecido não existir.
    """  # noqa: E501
    todo_item = await todo.get(db=db, id=id)
    if not todo_item:
        raise HTTPException(status_code=404, detail='Todo não encontrado')
    return todo_item
