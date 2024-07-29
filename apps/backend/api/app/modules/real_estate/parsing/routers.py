from celery.result import AsyncResult
from fastapi import APIRouter, BackgroundTasks, Query, Depends, HTTPException
from fastapi_pagination import Page, paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from starlette import status
from starlette.responses import JSONResponse

from app.tasks.celery import celery_app
from .repository import LinkRepository
from .schemas import ReadLinkSchema, NewLinkSchema, UpdateLinkSchema, FilterLinkSchema
from .utils.parsing_full_ads import ParsingFull
from app.tasks.tasks import parsing_full_data_ads_task

router = APIRouter()

disable_installed_extensions_check()


@router.get("/list", name="Список ссылок для парсинга")
# @cache(expire=10)
async def get_links(
        filters: FilterLinkSchema = Depends()
) -> Page[ReadLinkSchema]:
    """
    Получить список ссылок для парсинга.
    """
    try:
        links = await LinkRepository.get_all(**filters.dict())
        if not links:
            raise ValueError("В базе данных нет записей")
        return paginate(links)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}"
        )


@router.patch("/edit/{link_id}", name="Обновить ссылку")
async def update_link(link_id: int, link_update: UpdateLinkSchema = Depends()):
    """
    Обновить данные ссылки по ID.
    """
    link = await LinkRepository.get_one(id=link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")

    await LinkRepository.update(link_id, **link_update.model_dump())
    return {"message": "Ссылка успешно обновлена"}


@router.post("/add", name="Добавление новой ссылки")
async def add_link(link_data: NewLinkSchema = Depends()) -> dict:
    """
    Создание новой записи об объявлении


    :param link_data: данные для записи
    :return: dict
    """
    try:
        # получаем ссылку из базы данных
        # link = await LinkRepository.find_one_or_none(link=link_data.link)
        link = await LinkRepository.get_one(link=link_data.link)
        # если такая ссылка присутствует в БД
        if link:
            # выводим ошибку 500 с пояснением
            raise HTTPException(status_code=500, detail="Такая ссылка уже есть")
        # если ссылке в БД нет, то делаем новую запись
        await LinkRepository.create(**link_data.model_dump())
        return {"message": "Запись успешно создана", "error": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@router.delete("/delete/{id_link}", name="Удаление ссылки")
async def delete_link(id_link: int):
    """
    Удаление записи об объявлении


    :param id_link: данные для записи
    :return: dict
    """
    try:
        # получаем ссылку из базы данных
        link = await LinkRepository.get_one(id=id_link)
        # если такая ссылка присутствует в БД
        if not link:
            # выводим ошибку 500 с пояснением
            raise HTTPException(status_code=500, detail="Такого объявления нет")
        # если ссылка в БД, то удаяем её
        await LinkRepository.delete(id=id_link)
        return {"message": "Запись успешно удалена", "error": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


@router.get("/run/{link_id}", name="Запуск задачи парсинга")
async def start_task_parsing_ads(link_id: int):
    link = await LinkRepository.get_one(id=link_id)
    _link = {
        "id": link.id,
        "title": link.title,
        "link": link.link,
        "link_img": link.link_img,
        "price": link.price,
        "is_video": link.is_video
    }
    if link:
        task = parsing_full_data_ads_task.delay(_link)
        return JSONResponse({"task_id": task.id})
        # return {"message": "Задача запущена"}


@router.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id, app=celery_app)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)
