from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/planes", tags=["Planes"])


@router.get("/", response_model=list[schemas.Plan])
def listar_planes(db: Session = Depends(get_db)):
    return crud.obtener_planes(db)


@router.get("/{plan_id}", response_model=schemas.Plan)
def obtener_plan(
    plan_id: int,
    db: Session = Depends(get_db),
):
    plan = crud.obtener_plan(db, plan_id)

    if plan is None:
        raise HTTPException(status_code=404, detail="Plan no encontrado")

    return plan


@router.post("/", response_model=schemas.Plan, status_code=201)
def crear_plan(
    plan: schemas.PlanCreate,
    db: Session = Depends(get_db),
):
    return crud.crear_plan(db, plan)