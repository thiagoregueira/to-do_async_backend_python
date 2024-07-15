from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.todo import todo
from app.database.database import get_async_session
from app.schemas.todo import Todo, TodoCreate

router = APIRouter()


@router.post(
    '/', response_model=Todo, summary='Criar um novo to-do', status_code=201
)
async def create_todo(
    *, db: AsyncSession = Depends(get_async_session), todo_in: TodoCreate
) -> Todo:
    """
    Cria um novo Todo.
    Args:
    - db (AsyncSession): Dependência AsyncSession obtida através da função get_db para interagir com o banco de dados.
    - todo_in (TodoCreate): Dados de entrada para criar o Todo.
    Returns:
    - Todo: O objeto Todo criado.
    Raises:
    - HTTPException 400: Se os dados da requisição forem inválidos.
    """  # noqa: E501
    return await todo.create(db=db, obj_in=todo_in)
