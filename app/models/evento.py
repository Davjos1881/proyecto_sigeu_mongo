from beanie import Document, PydanticObjectId
from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime


class Organizacion(BaseModel):
    id_organizacion: Optional[Union[PydanticObjectId, str]] = None
    nombre_organizacion: Optional[str] = None


class Instalacion(BaseModel):
    id_instalacion: Optional[Union[PydanticObjectId, str]] = None
    nombre_instalacion: Optional[str] = None
    ubicacion: Optional[str] = None
    tipo_instalacion: Optional[str] = None


class Revision(BaseModel):
    id_revision: Optional[Union[PydanticObjectId, str]] = None
    estado: Optional[str] = None
    fecha_revision: Optional[datetime] = None
    justificacion: Optional[str] = None


class Aval(BaseModel):
    id_aval: Optional[Union[PydanticObjectId, str]] = None
    fecha_emision: Optional[datetime] = None
    emitido_por: Optional[str] = None
    rol_responsable: Optional[str] = None


class Responsable(BaseModel):
    usuario_id: Optional[Union[PydanticObjectId, str]] = None
    nombre_responsable: Optional[str] = None


class Certificado(BaseModel):
    id_certificado: Optional[Union[PydanticObjectId, str]] = None
    organizador_id: Optional[Union[PydanticObjectId, str]] = None
    representante: Optional[str] = None
    fecha_emision: Optional[datetime] = None


class Secretario(BaseModel):
    id_secretario: Optional[Union[PydanticObjectId, str]] = None
    nombre_secretario: Optional[str] = None
    unidad_id: Optional[Union[PydanticObjectId, str]] = None
    nombre_unidad: Optional[str] = None


class EventoModel(Document):
    id: Optional[PydanticObjectId] = None
    titulo: Optional[str] = None
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)  
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    publicado: bool = False
    organizacion: Optional[Organizacion] = None
    instalacion: Optional[Instalacion] = None
    revisiones: List[Revision] = Field(default_factory=list)
    avales: List[Aval] = Field(default_factory=list)
    responsables: List[Responsable] = Field(default_factory=list)
    unidad: Optional[Union[PydanticObjectId, str]] = None
    certificado_participacion: Certificado = Field(default_factory=Certificado) 
    secretario: Optional[Secretario] = None

    class Settings:
        name = "eventos"