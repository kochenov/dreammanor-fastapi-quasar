from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from app.core.database.database import get_async_session
from app.modules.auth_service.models import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(session: "AsyncSession" = Depends(get_async_session)):
    yield User.get_db(session=session)
