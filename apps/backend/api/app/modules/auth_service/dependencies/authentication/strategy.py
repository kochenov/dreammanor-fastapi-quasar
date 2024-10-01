from typing import (
    TYPE_CHECKING
)

from fastapi import Depends
from fastapi_users.authentication.strategy.db import (
    DatabaseStrategy,
)

from .access_tokens import get_access_tokens_db

if TYPE_CHECKING:
    from app.modules.auth_service.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
        access_tokens_db: "AccessTokenDatabase[AccessToken]" = Depends(get_access_tokens_db)) \
        -> DatabaseStrategy:
    # TODO вынести параметр в настройки
    return DatabaseStrategy(database=access_tokens_db, lifetime_seconds=3600)
