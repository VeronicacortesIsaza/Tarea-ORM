from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base
from pydantic import BaseModel, Field, PositiveInt, validator

class Habitacion(Base):
    __tablename__ = "habitaciones"

    id_habitacion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero = Column(Integer, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    disponible = Column(Boolean, default=True)

# ------------------ Pydantic Schemas ------------------

class HabitacionBase(BaseModel):
    numero: PositiveInt = Field(..., description="Número de la habitación")
    tipo: str = Field(..., min_length=3, max_length=50)
    precio: float = Field(..., gt=0)
    disponible: bool = True

    @validator("tipo")
    def validar_tipo(cls, v):
        if not v.strip():
            raise ValueError("El tipo de habitación no puede estar vacío")
        return v.strip().title()

class HabitacionCreate(HabitacionBase):
    pass

class HabitacionUpdate(BaseModel):
    tipo: str | None = Field(None, min_length=3, max_length=50)
    precio: float | None = Field(None, gt=0)
    disponible: bool | None = None

class HabitacionOut(HabitacionBase):
    id: int
    class Config:
        from_attributes = True

