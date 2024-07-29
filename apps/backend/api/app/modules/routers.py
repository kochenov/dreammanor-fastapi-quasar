from fastapi import APIRouter
from app.modules.real_estate.parsing.routers import router as parsing_routers
from app.modules.real_estate.houses.routers import router as homes_routers
# from app.modules.links.router import router as router_links
# from app.modules.parsing_process.router import router as router_process

routers = APIRouter()

routers.include_router(parsing_routers, prefix="/parsing", tags=["Ссылки"])
routers.include_router(homes_routers, prefix="/real-estate", tags=["Объявления"])
# api_router.include_router(router_process, tags=["parsing_process"])


