from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlmodel import create_engine, Session, SQLModel, Field

# Импортируем настройки из вашего файла конфигурации
from app.core.config import settings


# Создаем асинхронный движок базы данных на основе настроек
async_engine = create_async_engine(settings.database_url)

# Фабрика для создания асинхронных сессий
async_session_maker = async_sessionmaker(
    engine=async_engine, class_=AsyncSession, expire_on_commit=False
)


class Base(SQLModel):
    # __tablename__ = Field(default_factory=lambda cls: f"{cls.__name__.lower()}s")

    id: int = Field(default=None, primary_key=True)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Асинхронный генератор для получения сессии базы данных.
    """
    async with async_session_maker() as session:
        yield session
