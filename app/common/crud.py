from sqlalchemy import insert, select

from app.db import async_session_maker


class BaseCRUD:
    _model = None

    @classmethod
    async def get_obj_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls._model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_obj_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls._model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all_obj(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls._model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars()

    @classmethod
    async def create_obj(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls._model).values(**data).returning(cls._model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()
