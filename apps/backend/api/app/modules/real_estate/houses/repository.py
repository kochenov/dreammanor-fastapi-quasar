from app.core.database.base_repository import BaseRepository
from .models import Region


class RegionRepository(BaseRepository):
    model = Region
