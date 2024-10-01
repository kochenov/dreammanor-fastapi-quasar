from fastapi import APIRouter

from ..dependencies.authentication.backend import authentication_backend
from ..dependencies.authentication.fastapi_users_router import fastapi_users
from ..schemas.user_schemas import UserRead, UserCreate

router = APIRouter()
# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # обязательная верификация пользователя
        # requires_verification=True,
    ),
)


# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /request-verify-token
# /verify
router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
