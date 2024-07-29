import datetime
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy.dialects.postgresql import JSONB


class RegionBase(BaseModel):
    label: str


class RegionCreate(BaseModel):
    label: str


class RegionUpdate(RegionBase):
    pass


class AddOkey(BaseModel):
    status: str
    data: Optional[str] = None
    message: str


class RegionRead(RegionBase):
    class Config:
        from_attributes = True


class SettlemenTypeBase(BaseModel):
    label: str
    label_i: str


class SettlemenTypeCreate(SettlemenTypeBase):
    pass


class SettlemenTypeUpdate(SettlemenTypeBase):
    pass


class SettlemenTypeRead(SettlemenTypeBase):
    class Config:
        from_attributes = True


class DistrictBase(BaseModel):
    label: str
    region_id: int


class DistrictCreate(DistrictBase):
    pass


class DistrictUpdate(DistrictBase):
    pass


class DistrictRead(DistrictBase):
    class Config:
        from_attributes = True


class SettlementBase(BaseModel):
    settlement_types_id: int


class SettlementCreate(SettlementBase):
    pass


class SettlementUpdate(SettlementBase):
    pass


class SettlementListRead(SettlementBase):
    class Config:
        from_attributes = True


class SettlementRead(SettlementBase):
    class Config:
        from_attributes = True
