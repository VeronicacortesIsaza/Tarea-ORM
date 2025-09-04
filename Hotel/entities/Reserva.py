from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from typing import Annotated
from pydantic import BaseModel, PositiveInt, StringConstraints

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cliente = Column(String, nullable=False)
    documento = Column(String, nullable=False)
    noches = Column(Integer, nullable=False)

    habitacion_id = Column(Integer, ForeignKey("habitaciones.id"))
    habitacion = relationship("Habitacion")

class ReservaBase(BaseModel):
    cliente: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2)]
    documento: Annotated[str, StringConstraints(strip_whitespace=True, min_length=5)]
    noches: PositiveInt

class ReservaCreate(ReservaBase):
    habitacion_id: int

class ReservaUpdate(BaseModel):
    noches: PositiveInt | None = None

class ReservaOut(ReservaBase):
    id: int
    habitacion_id: int
    class Config:
        from_attributes = True

