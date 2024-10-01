from fastapi import APIRouter
from app.modules.real_estate.parsing.routers import router as parsing_routers
from app.modules.real_estate.houses.routers import router as homes_routers
from .auth_service.routers.route_auth import router as auth
from .auth_service.routers.route_user import router as users


routers = APIRouter()

routers.include_router(parsing_routers, prefix="/parsing", tags=["Ссылки"])
routers.include_router(homes_routers, prefix="/real-estate", tags=["Объявления"])
routers.include_router(auth, prefix="/auth-service", tags=["Аутентификация"])
routers.include_router(users, prefix="/auth-service", tags=["Пользователи"])
