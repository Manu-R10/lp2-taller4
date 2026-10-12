from sqlalchemy.orm import Session

from app import models, schemas


def obtener_planes(db: Session):
    return db.query(models.Plan).order_by(models.Plan.id).all()


def obtener_plan(db: Session, plan_id: int):
    return db.query(models.Plan).filter(models.Plan.id == plan_id).first()


def crear_plan(db: Session, plan: schemas.PlanCreate):
    db_plan = models.Plan(**plan.model_dump())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan


def obtener_miembros(db: Session, plan_id: int | None = None):
    consulta = db.query(models.Miembro)

    if plan_id is not None:
        consulta = consulta.filter(models.Miembro.plan_id == plan_id)

    return consulta.order_by(models.Miembro.id).all()


def obtener_miembro(db: Session, miembro_id: int):
    return (
        db.query(models.Miembro)
        .filter(models.Miembro.id == miembro_id)
        .first()
    )


def crear_miembro(db: Session, miembro: schemas.MiembroCreate):
    db_miembro = models.Miembro(**miembro.model_dump())
    db.add(db_miembro)
    db.commit()
    db.refresh(db_miembro)
    return db_miembro