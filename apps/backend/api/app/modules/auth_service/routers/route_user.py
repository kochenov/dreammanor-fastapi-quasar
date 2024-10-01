from fastapi import APIRouter

from app.modules.auth_service.dependencies.authentication.fastapi_users_router import (
    fastapi_users,
)
from app.modules.auth_service.schemas.user_schemas import UserRead, UserUpdate

router = APIRouter(prefix="/user")

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
