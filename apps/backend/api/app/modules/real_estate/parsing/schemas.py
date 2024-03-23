import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class FilterLinkSchema(BaseModel):
    status_id: Optional[int] = Field(None, ge=0, le=4)
    is_video: Optional[bool] = Field(None, description="Есть видео")
    min_price: int = Field(1, ge=0)
    max_price: int = Field(100000000, ge=0)

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        return {key: value for key, value in data.items() if value is not None}


# **Базовая модель ссылки**
class BaseLinkSchema(BaseModel):
    """
    Базовая модель для представления ссылки.

    **Атрибуты:**

    * `id`: Идентификатор ссылки (целое число).
    * `link`: Ссылка (строка, должна соответствовать regex `^https?://.*`).
    * `price`: Цена (целое число, должна быть больше 0).
    * `title`: Название (строка, максимальная длина 255 символов).
    * `status_id`: ID статуса (целое число).
    * `is_video`: Является ли видео (булев тип).
    * `comment`: Комментарий (строка, может быть None).
    * `link_img`: Ссылка на изображение (строка, может быть None).
    * `created_at`: Дата создания (дата-время).
    """

    id: int = Field(..., description="Идентификатор ссылки")
    link: str = Field(..., description="Ссылка")  # Required link with regex validation
    price: int = Field(..., gt=0, description="Цена")  # Price with positive value constraint
    title: str = Field(..., max_length=255, description="Название")  # Title with max length constraint
    status_id: int = Field(..., ge=0, le=4)
    is_video: Optional[bool] = Field(False, description="Есть ли видео")
    comment: Optional[str] = Field(None, description="Комментарий")
    link_img: Optional[str] = Field(None, description="Ссылка на изображение")
    created_ad: datetime.datetime

    class Config:
        from_attributes = True


# **Модель для создания новой ссылки**
class NewLinkSchema(BaseModel):
    """
    Модель для создания новой ссылки.

    **Наследует все атрибуты и методы из `BaseModel`.**
    """

    link: str = Field(..., title="Ссылка")
    price: int
    title: str
    status_id: int = Field(0, ge=0, le=4)
    is_video: bool
    comment: Optional[str] = None
    link_img: Optional[str] = None

    class Config:
        from_attributes = True


# **Модель для чтения ссылки**
class ReadLinkSchema(BaseLinkSchema):
    """
    Модель для чтения информации о ссылке.

    **Наследует все атрибуты и методы из `BaseLinkSchema`.**
    """

    pass


# **Модель для обновления ссылки**
class UpdateLinkSchema(BaseModel):
    """
    Модель для обновления информации о ссылке.

    **Атрибуты:**

    * `status_id`: Новый ID статуса (целое число).
    * `comment`: Новый комментарий (строка, может быть None).
    """

    status_id: int = Field(..., ge=0, le=4)
    comment: Optional[str] = Field(None, description="Новый комментарий")

    class Config:
        title = "Модель обновления ссылки"
