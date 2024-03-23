from fastapi import APIRouter, BackgroundTasks, Query, Depends, HTTPException
from fastapi_pagination import Page, paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from starlette import status

from .repository import LinkRepository
from .schemas import ReadLinkSchema, NewLinkSchema, UpdateLinkSchema, FilterLinkSchema

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


@router.delete("/delite/{id_link}", name="Удаление ссылки")
async def delite_link(id_link: int):
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
