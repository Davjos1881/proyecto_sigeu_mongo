from fastapi import APIRouter, status
from typing import List

from app.crud import evento_crud as crud

router = APIRouter()


try:
    from app.schemas.evento_schema import EventoCrear, Evento, EventoActualizar
except ImportError:
    from app.schemas.evento import EventoCrear, Evento, EventoActualizar


@router.post("/", response_model=Evento, status_code=status.HTTP_201_CREATED)
async def crear_evento(nuevo: EventoCrear):
    return await crud.crear_evento(nuevo)


@router.get("/", response_model=List[Evento], status_code=status.HTTP_200_OK)
async def listar_eventos():
    return await crud.listar_eventos()


@router.get("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def obtener_evento(evento_id: str):
    return await crud.obtener_evento_por_id(evento_id)


@router.put("/{evento_id}", response_model=Evento, status_code=status.HTTP_200_OK)
async def actualizar_evento(evento_id: str, datos: EventoActualizar):
    return await crud.actualizar_evento(evento_id, datos)


@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_evento(evento_id: str):
    await crud.eliminar_evento(evento_id)
