from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Any
from datetime import datetime

class Estudiante(BaseModel):
    programa_id: Optional[Any] = None
    nombre_programa: Optional[str] = None


class Docente(BaseModel):
    unidad_id: Optional[Any] = None
    nombre_unidad: Optional[str] = None


class Perfil(BaseModel):
    estudiante: Optional[Estudiante] = None
    docente: Optional[Docente] = None


class Contrasena(BaseModel):
    id_contrasena: Optional[int] = None
    fecha_creacion: datetime
    fecha_ultimo_cambio: datetime
    vigente: bool


class Notificacion(BaseModel):
    id_notificacion: Optional[Any] = None
    evento_id: Optional[Any] = None
    mensaje: Optional[str] = None
    fecha: Optional[datetime] = None



class UsuarioModel(Document):
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    rol_usuario: str

    perfil: Perfil = Perfil()

    contrasenas: List[Contrasena] = []
    notificaciones: List[Notificacion] = []

    class Settings:
        name = "usuarios"