# modules/real_estate/parsing/repository.py

from sqlalchemy import select

from app.core.database.base_repository import BaseRepository
from app.core.database.database import async_session_maker
from .models import Link, Process


class LinkRepository(BaseRepository):
    """Репозиторий для работы с объявлениями недвижимости.

    Предоставляет методы для:
        * Получения объявлений по различным критериям
        * Добавления новых объявлений
        * Обновления информации об объявлениях
        * Удаления объявлений

    Пример использования:

    ```python
    from modules.real_estate.parsing.repository import LinkRepository

    # Получить все объявления
    link_repository = LinkRepository()
    all_links = link_repository.get_all()

    # Получить последнее объявление
    last_link = link_repository.get_last()

    # Добавить новое объявление
    new_link = Link(link="[неправильный URL удален]", price=1000000)
    link_repository.add(new_link)

    # Обновить информацию об объявлении
    link_repository.update(link_id=1, price=1200000)

    # Удалить объявление
    link_repository.delete(link_id=1)
    ```
    """

    model = Link

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
        min_price = filters.pop("min_price", None)
        max_price = filters.pop("max_price", None)

        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter_by(**filters)
                .filter(cls.model.price.between(min_price, max_price))
                .order_by(cls.model.id.desc())
            )

            result = await session.execute(query)
            return result.mappings().all()


class ProcessRepository(BaseRepository):
    """Репозиторий для работы с записями о процессе парсинга.

    Предоставляет методы для:
        * Получения записей о процессе парсинга по различным критериям
        * Добавления новых записей о процессе парсинга
        * Обновления информации о записях о процессе парсинга
        * Удаления записей о процессе парсинга

    Пример использования:

    ```python
    from modules.real_estate.parsing.repository import ProcessRepository

    # Получить все записи о процессе парсинга
    process_repository = ProcessRepository()
    all_processes = process_repository.get_all()

    # Получить последнюю запись о процессе парсинга
    last_process = process_repository.get_last()

    # Добавить новую запись о процессе парсинга
    new_process = Process(iterate=1, page=1)
    process_repository.add(new_process)

    # Обновить информацию о записи о процессе парсинга
    process_repository.update(process_id=1, iterate=2)

    # Удалить запись о процессе парсинга
    process_repository.delete(process_id=1)
    ```
    """

    model = Process
