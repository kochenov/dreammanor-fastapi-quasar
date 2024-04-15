import datetime
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy.dialects.postgresql import JSONB


class FilterLinkSchema(BaseModel):
    status_id: Optional[int] = Field(None, ge=0, le=4)
    is_video: Optional[bool] = Field(None, description="Есть видео")
    min_price: int = Field(1, ge=0)
    max_price: int = Field(100000000, ge=0)

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        return {key: value for key, value in data.items() if value is not None}


# **Базовая модель ссылки**
class HouseSchema(BaseModel):
    id: int = Field(..., description="Идентификатор объявления")
    link: str = Field(..., description="Ссылка на Авито")  # Required link with regex validation

    # 0 - загружен
    # 1 - опубликован
    # 2 - черновик
    # 3 - запланированная публикация
    # 4 - объявление не актуально
    status_id: int = Field(..., ge=0, le=4, description="Статус объявления")
    price: int = Field(..., gt=0, description="Цена")  # Price with positive value constraint
    title: str = Field(..., max_length=255, description="Название объявления")  # Title with max length constraint
    is_video: bool = Field(False, description="Наличие видео")
    comment: Optional[str] = Field(None, description="Комментарий к публикации")
    link_img: Optional[str] = Field(None, description="Ссылка на изображение")
    created_ad: datetime.datetime
    data: JSONB

    class Config:
        from_attributes = True

