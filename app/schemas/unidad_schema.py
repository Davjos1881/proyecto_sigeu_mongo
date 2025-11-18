from pydantic import BaseModel, Field
from typing import Optional, Union
from beanie import PydanticObjectId


class FacultadRef(BaseModel):
    id_facultad: Optional[Union[str, PydanticObjectId]] = None
    nombre_facultad: Optional[str] = None


class UnidadCrear(BaseModel):
    nombre_unidad: str
    facultad: Optional[FacultadRef] = None


class Unidad(BaseModel):
    id: Optional[Union[str, PydanticObjectId]] = Field(
        None, description="ID de la unidad"
    )
    nombre_unidad: str
    facultad: Optional[FacultadRef] = None


class UnidadActualizar(BaseModel):
    nombre_unidad: Optional[str] = None
    facultad: Optional[FacultadRef] = None