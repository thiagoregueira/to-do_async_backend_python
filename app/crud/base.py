# app/crud/base.py
from typing import Any, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database.base import Base

ModelType = TypeVar('ModelType', bound='Base')
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        Objeto CRUD com métodos padrão para Criar, Ler, Atualizar e Deletar (CRUD).
        **Parâmetros**
        * `model`: Uma classe de modelo SQLAlchemy
        """  # noqa: E501
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        """
        Recupera um único registro pelo seu ID.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `id`: O ID do registro a ser recuperado
        **Retorna**
        O registro recuperado ou `None` se não encontrado.
        """
        result = await db.execute(
            select(self.model).filter(self.model.id == id)
        )
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """
        Recupera vários registros com paginação.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `skip`: O número de registros a serem pulados (padrão é 0)
        * `limit`: O número máximo de registros a serem retornados (padrão é 100)
        **Retorna**
        Uma lista de registros recuperados.
        """  # noqa: E501
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(
        self, db: AsyncSession, *, obj_in: CreateSchemaType
    ) -> ModelType:
        """
        Cria um novo registro.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `obj_in`: Os dados para o novo registro
        **Retorna**
        O registro criado.
        """
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(  # noqa: PLR6301
        self, db: AsyncSession, *, db_obj: ModelType, obj_in: UpdateSchemaType
    ) -> ModelType:
        """
        Atualiza um registro existente.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `db_obj`: O registro existente a ser atualizado
        * `obj_in`: Os novos dados para o registro
        **Retorna**
        O registro atualizado.
        """
        obj_data = db_obj.__dict__
        update_data = obj_in.model_dump(exclude_defaults=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *, id: int) -> ModelType:
        """
        Deleta um registro pelo seu ID.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `id`: O ID do registro a ser deletado
        **Retorna**
        O registro deletado.
        """
        obj = await self.get(db, id)
        await db.delete(obj)
        await db.commit()
        return obj

    async def increment_views(self, db: AsyncSession, *, id: int) -> None:
        """
        Incrementa a contagem de visualizações de um registro.
        **Parâmetros**
        * `db`: A sessão do banco de dados
        * `id`: O ID do registro para incrementar as visualizações
        **Retorna**
        None
        """
        await db.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(views=self.model.views + 1)
        )
        await db.commit()
