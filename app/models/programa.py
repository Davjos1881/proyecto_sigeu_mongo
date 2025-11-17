from beanie import Document, PydanticObjectId
from pydantic import BaseModel
from typing import Optional


class Facultad(BaseModel):
    id_facultad: Optional[PydanticObjectId]  
    nombre_facultad: Optional[str]           


class ProgramaModel(Document):
    nombre_programa: str
    facultad: Facultad                       

    class Settings:
        name = "programas"