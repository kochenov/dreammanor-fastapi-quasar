from sqlalchemy import select, insert, delete, update

from .database import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filters):
        """Получить записи согласно фильтрам"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_last(cls, **filters):
        """Получить последнюю запись согласно фильтрам"""
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filters)
                .order_by(cls.model.id.desc())
                .limit(1)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filters):
        """Получить все записи"""
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filters)
                .order_by(cls.model.id.desc())
            )

            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        """Добавить запись"""
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id: int, **data):
        """Обновить запись по ID"""
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
