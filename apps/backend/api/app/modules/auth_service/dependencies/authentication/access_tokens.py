from typing import TYPE_CHECKING

from fastapi import Depends

from app.core.database.database import get_async_session
from app.modules.auth_service.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_tokens_db(session: "AsyncSession" = Depends(get_async_session)):
    yield AccessToken.get_db(session=session)
