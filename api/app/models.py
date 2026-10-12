from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Plan(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    precio = Column(Float, nullable=False)
    duracion_dias = Column(Integer, nullable=False)

    miembros = relationship("Miembro", back_populates="plan")


class Miembro(Base):
    __tablename__ = "miembros"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    telefono = Column(String(20), nullable=False)

    plan_id = Column(Integer, ForeignKey("planes.id"), nullable=False)
    plan = relationship("Plan", back_populates="miembros")