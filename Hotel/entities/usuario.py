from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base
from pydantic import BaseModel, Field, PositiveInt, validator

class Usuario():
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    primer_apellido = Column(String, nullable=False)
    segundo_apellido = Column(String, nullable=False)
    nombre_usuario = Column(String, default=True)

