from typing import List, Optional
from fastapi import APIRouter, status, Query, Path, HTTPException
from app import crud
from app.schemas.evento_schema import (
    Evento,EventoCrear,
    EventoActualizar,
    Revision,
    Aval,
    Responsable,
    CertificadoParticipacion,
)
from app.crud import evento_crud

router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.post("/", response_model=Evento, status_code=status.HTTP_201_CREATED)
async def crear_evento(data: EventoCrear):
    return await evento_crud.crear_evento(data)


@router.get("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def obtener_evento(evento_id: str = Path(..., description="ID del evento")):
    return await evento_crud.obtener_evento_por_id(evento_id)


@router.get("/", response_model=List[Evento], status_code=status.HTTP_200_OK)
async def listar_eventos():
    return await evento_crud.listar_eventos()


@router.put("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def actualizar_evento(evento_id: str, datos: EventoActualizar):
    return await evento_crud.actualizar_evento(evento_id, datos)


@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_evento(evento_id: str):
    await evento_crud.eliminar_evento(evento_id)
    return None


# --- documentos embebidos ---------------------------------

@router.post("/{evento_id}/revisiones", response_model=Revision, status_code=status.HTTP_201_CREATED)
async def agregar_revision(evento_id: str, revision: Revision):
    return await evento_crud.agregar_revision(evento_id, revision)


@router.put("/{evento_id}/revisiones/{revision_id}", status_code=status.HTTP_204_NO_CONTENT)
async def actualizar_revision(evento_id: str, revision_id: str):
    await evento_crud.actualizar_revision(evento_id, revision_id)
    return None


@router.post("/{evento_id}/avales", response_model=Aval, status_code=status.HTTP_201_CREATED)
async def agregar_aval(evento_id: str, aval: Aval):
    return await evento_crud.agregar_aval(evento_id, aval)


@router.delete("/{evento_id}/avales/{aval_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_aval(evento_id: str, aval_id: str):
    await evento_crud.eliminar_aval(evento_id, aval_id)
    return None


@router.post("/{evento_id}/responsables", response_model=Responsable, status_code=status.HTTP_201_CREATED)
async def agregar_responsable(evento_id: str, responsable: Responsable):
    return await evento_crud.agregar_responsable(evento_id, responsable)


@router.delete("/{evento_id}/responsables/{responsable_idx}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_responsable(evento_id: str, responsable_idx: int = Path(..., description="Índice o id del responsable")):
    await evento_crud.eliminar_responsable(evento_id, responsable_idx)
    return None


@router.put("/{evento_id}/certificado", response_model=CertificadoParticipacion, status_code=status.HTTP_200_OK)
async def agregar_certificado(evento_id: str, certificado: CertificadoParticipacion):
    return await evento_crud.agregar_certificado_participacion(evento_id, certificado)


@router.delete("/{evento_id}/certificado", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_certificado(evento_id: str):
    """Quitar/eliminar el certificado_participacion del evento."""
    await evento_crud.eliminar_certificado(evento_id)
    return None