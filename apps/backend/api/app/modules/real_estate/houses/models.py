import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database.database import BaseModel


class Region(BaseModel):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)


class Districts(BaseModel):
    __tablename__ = "districts"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)  # Область


class SettlementType(BaseModel):
    __tablename__ = "settlement_types"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False, unique=True)
    label_i = Column(String(255), nullable=False, unique=True)  # (где) в городе


class Settlements(BaseModel):
    __tablename__ = "settlements"
    id = Column(Integer, primary_key=True)
    label = Column(String(255), nullable=False)
    label_i = Column(String(255), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"))  # Область
    district_id = Column(Integer, ForeignKey("districts.id"))  # Район
    settlement_types_id = Column(Integer, ForeignKey("settlement_types.id"))
    settlement_type = relationship("SettlementType")
