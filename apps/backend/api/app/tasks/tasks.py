import asyncio

from app.tasks.celery import celery_app
from app.modules.real_estate.parsing.utils.process import Process


# Импорт Celery application object
@celery_app.task(
    name="parsing_links_task",
    ignore_result=True,
)
def parsing_links_task():

    # Создание объекта Process
    # Параметры: sort=True, agent=False
    process = Process(sort=True, agent=False)

    # Получение цикла событий
    loop = asyncio.get_event_loop()

    # Запуск process.run() в асинхронном режиме
    # Возвращает результат выполнения process.run()
    return loop.run_until_complete(process.run())
