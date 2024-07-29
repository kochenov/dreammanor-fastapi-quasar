from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from fastapi import HTTPException
from sqlalchemy.orm import exc
from sqlalchemy.exc import IntegrityError

from .repository import RegionRepository
from .schemas import RegionCreate

router = APIRouter()


# disable_installed_extensions_check()


# Regions
@router.get("/regions/", name="Регионы")
async def read_regions():
    try:
        regions = await RegionRepository.get_all()
        if not regions:
            raise ValueError("В базе данных нет записей")
        return regions
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}"
        )


@router.post("/regions/add", name="Добавление нового региона")
async def add_new_region(region: RegionCreate = Depends()) -> dict:
    """
    Создание нового региона

    :param region: данные для записи
    :return: dict
    """
    try:
        # если ссылки в БД нет, то делаем новую запись
        await RegionRepository.create(**region.model_dump())
        return {"message": "Запись успешно создана", "error": None}
    except IntegrityError as e:
        # Проверка на конкретное нарушение ограничения
        if "duplicate key value violates unique constraint" in str(e):
            raise HTTPException(status_code=409,
                                detail="Ошибка: Запись с таким же значением в столбце 'label' уже существует.")
        # Обработка других исключений IntegrityError (необязательно)
        # ...
    except Exception as e:
        # Обработка других непредвиденных исключений
        raise HTTPException(status_code=500, detail=f"{e}")


@router.delete("/delite/{id}", name="Удаление региона")
async def delite_region(id: int):
    """
    Удаление записи об объявлении

    Args:
        id:
    """
    try:
        # получаем ссылку из базы данных
        link = await RegionRepository.get_one(id=id)
        # если такая ссылка присутствует в БД
        if not link:
            # выводим ошибку 500 с пояснением
            raise HTTPException(status_code=500, detail="Такого региона нет")
        # если ссылка в БД, то удаляем её
        await RegionRepository.delete(id=id)
        return {"message": "Запись успешно удалена", "error": None}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
