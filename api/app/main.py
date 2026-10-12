from fastapi import FastAPI

from app.database import Base, engine
from app.routers import miembros, planes

# Importar los modelos para registrar las tablas en SQLAlchemy.
from app import models  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GYM RAI API",
    description="API para administrar los planes y miembros de GYM RAI.",
    version="1.0.0",
)

app.include_router(miembros.router)
app.include_router(planes.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "Bienvenido a la API de GYM RAI"}


@app.get("/health", tags=["Salud"])
def health():
    return {"estado": "ok"}