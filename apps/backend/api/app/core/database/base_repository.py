from sqlalchemy import select, insert, delete, update

from .database import async_session_maker


class BaseRepository:
    """Базовый класс для репозиториев SQLAlchemy с асинхронными методами.

    Предназначен для наследования конкретными репозиториями моделей,
    предоставляя общие методы работы с базой данных.
    """

    model = None  # Обязательное поле - модель SQLAlchemy, для которой предназначен репозиторий

    @classmethod
    async def get_one(cls, **filters):
        """Получить одну запись по заданным фильтрам.

        Возвращает найденную запись (экземпляр модели)
        или None, если запись не найдена.

        Args:
            filters (dict): Словарь фильтров для поиска записи.
                Ключи словаря соответствуют столбцам модели,
                значения - фильтруемым значениям.

        Returns:
            Model | None: Экземпляр модели или None.
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_last(cls, **filters):
        """Получить последнюю запись по заданным фильтрам.

        Возвращает последнюю найденную запись (экземпляр модели)
        или None, если записей не найдено.

        Args:
            filters (dict): Словарь фильтров для поиска записи.
                Ключи словаря соответствуют столбцам модели,
                значения - фильтруемым значениям.

        Returns:
            Model | None: Экземпляр модели или None.
        """
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filters)
                .order_by(cls.model.id.desc())
                .limit(1)
            )
            return await session.execute(query).scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filters):
        """Получить все записи по заданным фильтрам.

        Возвращает список найденных записей (список экземпляров модели).

        Args:
            filters (dict): Словарь фильтров для поиска записей.
                Ключи словаря соответствуют столбцам модели,
                значения - фильтруемым значениям.

        Returns:
            list[Model]: Список экземпляров модели.
        """
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filters)
                .order_by(cls.model.id.desc())
            )

            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def create(cls, **data):
        """Создать новую запись в базе данных.

        Создает новую запись на основе переданных данных и
        возвращает ее (экземпляр модели).

        Args:
            data (dict): Словарь данных для создания новой записи.
                Ключи словаря соответствуют столбцам модели,
                значения - данным для новой записи.

        Returns:
            Model: Экземпляр созданной модели.
        """
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            # Возвращаем только что созданную запись для удобства
            return await session.get(cls.model, data.get("id"))

    @classmethod
    async def update(cls, model_id: int, **data):
        """Обновить существующую запись по ее ID.

        Обновляет запись с указанным ID на основе переданных данных.

        Args:
            model_id (int): ID записи для обновления.
            data (dict): Словарь данных для обновления записи.
                Ключи словаря соответствуют столбцам модели,
                значения - новыми данными для записи.
        """
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filters):
        """Удалить записи по заданным фильтрам.

                Args:
                    filters (dict): Словарь фильтров для удаления записей.
                        Ключи словаря соответствуют столбцам модели,
                        значения - фильтруемым значениям.
                """
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filters)
            await session.execute(query)
            await session.commit()
