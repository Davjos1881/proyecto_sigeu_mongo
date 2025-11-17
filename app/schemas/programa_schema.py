from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson import ObjectId


class FacultadRef(BaseModel):
    id_facultad: Optional[str] = None
    nombre_facultad: Optional[str] = None

    @field_validator("id_facultad", mode="before")
    def validar_id_facultad(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v


class ProgramaCrear(BaseModel):
    nombre_programa: str
    facultad: Optional[FacultadRef] = None


class Programa(BaseModel):
    id: str = Field(..., description="ID del programa")
    nombre_programa: str
    facultad: Optional[FacultadRef] = None

    @field_validator("id", mode="before")
    def validar_id(cls, v):
        if isinstance(v, ObjectId):
            return str(v)
        return v


class ProgramaActualizar(BaseModel):
    nombre_programa: Optional[str] = None
    facultad: Optional[FacultadRef] = None