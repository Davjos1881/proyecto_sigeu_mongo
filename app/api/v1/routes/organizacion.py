from fastapi import APIRouter, status
from typing import List, Optional

from app.schemas.organizacion import (
    OrganizacionCrear,
    Organizacion,
    OrganizacionActualizar,
)
from app.crud import organizacion_crud as crud

router = APIRouter()




@router.post(
    "/",
    response_model=Organizacion,
    status_code=status.HTTP_201_CREATED
)
async def crear_organizacion(nueva: OrganizacionCrear):
    return await crud.crear_organizacion(nueva)





@router.get(
    "/",
    response_model=List[Organizacion],
    status_code=status.HTTP_200_OK
)
async def listar_organizaciones(q: Optional[str] = None):
    return await crud.listar_organizaciones(q)




@router.get(
    "/{organizacion_id}",
    response_model=Organizacion,
    status_code=status.HTTP_200_OK
)
async def obtener_organizacion(organizacion_id: str):
    return await crud.obtener_organizacion_por_id(organizacion_id)





@router.put(
    "/{organizacion_id}",
    response_model=Organizacion,
    status_code=status.HTTP_200_OK
)
async def actualizar_organizacion(organizacion_id: str, datos: OrganizacionActualizar):
    return await crud.actualizar_organizacion(organizacion_id, datos)





@router.delete(
    "/{organizacion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def eliminar_organizacion(organizacion_id: str):
    await crud.eliminar_organizacion(organizacion_id)
    return None
