import json
from pathlib import Path

from sqlalchemy.orm import Session

from app import models
from app.database import Base, SessionLocal, engine

SEED_FILE = Path(__file__).resolve().parent.parent / "data" / "seed.json"


def cargar_datos(db: Session):
    with SEED_FILE.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    planes_por_nombre = {}

    for datos_plan in datos["planes"]:
        plan = (
            db.query(models.Plan)
            .filter(models.Plan.nombre == datos_plan["nombre"])
            .first()
        )

        if plan is None:
            plan = models.Plan(**datos_plan)
            db.add(plan)
            db.flush()

        planes_por_nombre[plan.nombre] = plan

    for datos_miembro in datos["miembros"]:
        nombre_plan = datos_miembro["plan"]
        plan = planes_por_nombre.get(nombre_plan)

        if plan is None:
            raise ValueError(f"No existe el plan: {nombre_plan}")

        miembro = (
            db.query(models.Miembro)
            .filter(
                models.Miembro.nombre == datos_miembro["nombre"],
                models.Miembro.telefono == datos_miembro["telefono"],
            )
            .first()
        )

        if miembro is None:
            nuevo_miembro = models.Miembro(
                nombre=datos_miembro["nombre"],
                edad=datos_miembro["edad"],
                telefono=datos_miembro["telefono"],
                plan_id=plan.id,
            )
            db.add(nuevo_miembro)

    db.commit()


def main():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        cargar_datos(db)
        print("Datos iniciales cargados correctamente.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()