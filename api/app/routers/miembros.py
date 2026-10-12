from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/miembros", tags=["Miembros"])


@router.get("/", response_model=list[schemas.Miembro])
def listar_miembros(
    plan_id: int | None = Query(default=None, gt=0),
    db: Session = Depends(get_db),
):
    return crud.obtener_miembros(db, plan_id=plan_id)


@router.get("/{miembro_id}", response_model=schemas.Miembro)
def obtener_miembro(
    miembro_id: int,
    db: Session = Depends(get_db),
):
    miembro = crud.obtener_miembro(db, miembro_id)

    if miembro is None:
        raise HTTPException(status_code=404, detail="Miembro no encontrado")

    return miembro


@router.post("/", response_model=schemas.Miembro, status_code=201)
def crear_miembro(
    miembro: schemas.MiembroCreate,
    db: Session = Depends(get_db),
):
    if crud.obtener_plan(db, miembro.plan_id) is None:
        raise HTTPException(status_code=404, detail="Plan no encontrado")

    return crud.crear_miembro(db, miembro)