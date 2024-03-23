import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime

from app.core.database.database import BaseModel


class Link(BaseModel):
    """Описание таблицы базы данных объявлений недвижимости при парсинге"""

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=True)
    title = Column(String, nullable=False)
    status_id = Column(Integer, default=0)
    is_video = Column(Boolean, default=False)
    comment = Column(String, nullable=True, default=None)
    link_img = Column(String, nullable=True, default=None)
    created_ad = Column(DateTime, default=datetime.datetime.now())


class Process(BaseModel):
    """Описание таблицы базы данных процесса парсинга"""
    __tablename__ = "process"
    id = Column(Integer, primary_key=True)
    iterate = Column(Integer, default=0)
    page = Column(Integer, default=1)
    error = Column(Boolean, default=False)
    created_ad = Column(DateTime, default=datetime.datetime.now())