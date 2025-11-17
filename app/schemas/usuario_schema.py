from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class Estudiante(BaseModel):
    programa_id: Optional[str] = None
    nombre_programa: Optional[str] = None


class Docente(BaseModel):
    unidad_id: Optional[str] = None
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
    id_notificacion: Optional[str] = None
    evento_id: Optional[str] = None
    mensaje: Optional[str] = None
    fecha: Optional[datetime] = None


class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    rol_usuario: str

    perfil: Optional[Perfil] = None  
    


class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    rol_usuario: Optional[str] = None

    perfil: Optional[Perfil] = None  


class Usuario(BaseModel):
    id: str = Field(..., description="ID del usuario")

    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    rol_usuario: str

    perfil: Optional[Perfil] = None

    contrasenas: List[Contrasena] = Field(default_factory=list)
    notificaciones: List[Notificacion] = Field(default_factory=list)