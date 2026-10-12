from pydantic import BaseModel, ConfigDict, Field


class PlanBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    precio: float = Field(gt=0)
    duracion_dias: int = Field(gt=0)


class PlanCreate(PlanBase):
    pass


class Plan(PlanBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class MiembroBase(BaseModel):
    nombre: str = Field(min_length=2, max_length=100)
    edad: int = Field(ge=16, le=100)
    telefono: str = Field(min_length=7, max_length=20)
    plan_id: int = Field(gt=0)


class MiembroCreate(MiembroBase):
    pass


class Miembro(MiembroBase):
    id: int

    model_config = ConfigDict(from_attributes=True)