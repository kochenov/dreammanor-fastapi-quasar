from starlette.responses import JSONResponse

from app.core.logger import logger
from .avito_url_generator_links import AvitoURLGenerator
from .parsing import Parsing
from ..repository import ProcessRepository, LinkRepository


class Process:
    """
    Класс для запуска процесса парсинга страниц Авито.


    Атрибуты:
        sort (bool): Включение сортировки
        agent (bool): Включение к выдачи агенств
        _list_urls (list): Список URL-ов для обработки.
        _current_iterate (int): Текущая итерация обработки.
        _current_page (int): Текущая страница обработки.
        _error (bool): Флаг ошибки в процессе обработки.
    """

    sort: bool
    agent: bool
    _list_urls: list
    _current_iterate: int = 0
    _current_page: int = 1
    _error: bool = False

    # инициализация класса
    def __init__(self, sort: bool, agent: bool):
        """
        Запуск процесса парсинга страниц Авито.

        :param sort: Сортировка
        :param agent: Агентства
        """
        self.sort = sort
        self.agent = agent

        self._list_urls = self.__get_parsing_links()

    def __get_parsing_links(self) -> list:
        """
        :return (list): список ссылок для парсинга
        """
        return AvitoURLGenerator(sort=self.sort, agent=self.agent).generate_all_urls()

    async def run(self):
        """
        Запуск процесса получения данных объявлений
        """
        try:
            logger.info("process: Запуск процесса получения данных объявлений")
            # 1 - получение данных и инициализация значений
            await self._get_record_last()

            # 2 - старт парсинга
            await self._start_parsing_lists_ads(self._list_urls[self._current_iterate])
            logger.info("process: Запуск процесса получения данных объявлений успешен")
            return "Конец"
        except Exception as e:
            logger.warning(f"process: Запуск процесса получения данных с ошибкой: {e}")
            return "Ошибка!!!!"

    async def _get_record_last(self) -> None:
        """
        Метод получает последнюю запись о процессе
        парсинга из базы данных и инициализирует свойства
        класса
        """
        try:
            logger.info("process: Получить запись из БД о последней сессии")
            # получить последнюю запись из БД
            record_item_process = await ProcessRepository.get_last()

            # если в БД есть запись
            # присваиваю данные атрибутам объекта
            # если записи ещё нет, значения остаются по умолчанию
            if record_item_process is not None:
                logger.info(f"process: Запись из БД о последней сессии получена: ID {record_item_process.id}")
                self._init_property(
                    iterate=record_item_process.iterate,
                    page=record_item_process.page,
                    error=record_item_process.error,
                )
                logger.info(f"process: Инициализация данных процесса успешна пройдена")
        except Exception as e:
            logger.warning(f"Ошибка при получении последней записи о процессе: {e}")

    def _init_property(self, iterate: int, page: int, error: bool) -> None:
        """Инициализация свойств объекта"""
        try:

            self._current_iterate = iterate
            self._current_page = (
                page + 1 if not error else page
            )  # если есть ошибка оставим как есть
            self._error = error
            if error:
                logger.info(
                    f"[process]...\nВ последней записи есть ошибка:\nУстанавливаю: \n    Итерация [{self._current_iterate}]\n    "
                    f"Страница [{self._current_page}]")
            else:
                logger.info(
                    f"[process]...\nУстанавливаю: \n    Итерация [{self._current_iterate}]\n    "
                    f"Страница [{self._current_page}]")
        except Exception as e:
            logger.warning(f"process: В инициализации свойств объекта произошла ошибка: \n{e}")

    async def _start_parsing_lists_ads(self, link: str):
        """
        Старт парсинга страницы
        :param link: ссылка для парсинга
        :return:
        """
        try:
            logger.info("process: Запущен процесс парсинга")
            parsing = Parsing(url=link, num_page=self._current_page)
            logger.info("process: Узнаём количество страниц")
            count_pages = parsing.count_page
            logger.info(f"process: Количество страниц {count_pages} ")
            # Если число текущей страница больше общего количества страниц
            if self._current_page > count_pages:
                # увеличиваем итерацию
                if self._current_iterate + 1 > len(self._list_urls):
                    self._current_iterate = 0
                else:
                    self._current_iterate += 1
                # скидываем текущую страницу
                self._current_page = 1
                # сохраняем
                logger.info("process: Сохраняем процесс в базу")
                await ProcessRepository.create(
                    iterate=self._current_iterate, page=self._current_page, error=True
                )
                logger.info("process: Процесс в базу успешно сохранён")
                return
            # Получить данные о ссылке
            logger.info("process: Процесс получения данных о ссылке начат")
            link_data = parsing.get_ads_link_data()
            logger.info("process: Процесс получения данных о ссылке успешен")
            # если пусто есть ошибка (True)
            self._error = not len(link_data)
            # сохранить ссылку
            for item in link_data:
                existing_link = await LinkRepository.get_one(link=item["link"])
                if existing_link is None:
                    await LinkRepository.create(
                        link=item["link"],
                        price=item["price"],
                        title=item["title"],
                        is_video=item["is_video"],
                        link_img=item["link_img"],
                    )
                    logger.info("process: Информация о ссылке успешно сохранена в БД")

            await ProcessRepository.create(
                iterate=self._current_iterate,
                page=self._current_page,
                error=self._error,
            )
            logger.info("Процесс парсинга успешно окончен")
            return True
        except Exception as e:
            await ProcessRepository.create(
                iterate=self._current_iterate, page=self._current_page, error=True
            )
            raise Exception(f"Не удалось сделать парсинг страницы / {e}")
