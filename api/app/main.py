from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
from app.routers import miembros, planes

# Importar los modelos para registrar las tablas en SQLAlchemy.
from app import models  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GYM RAI API",
    description="API para administrar los planes y miembros de GYM RAI.",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
)

STATIC_DIR = Path(__file__).resolve().parent / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/docs", include_in_schema=False)
def documentacion_personalizada():
    respuesta = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="GYM RAI API - Documentación",
    )

    html = respuesta.body.decode("utf-8")
    html = html.replace(
        "</head>",
        '<link rel="stylesheet" href="/static/swagger-dark.css"></head>',
    )

    return HTMLResponse(content=html)


app.include_router(miembros.router)
app.include_router(planes.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "Bienvenido a la API de GYM RAI"}


@app.get("/health", tags=["Salud"])
def health():
    return {"estado": "ok"}