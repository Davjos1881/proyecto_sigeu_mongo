from fastapi import APIRouter, status
from typing import List

from app.schemas.instalacion import InstalacionCrear, Instalacion, InstalacionActualizar
from app.crud import instalaciones_crud as crud

router = APIRouter()



@router.post(
    "/",
    response_model=Instalacion,
    status_code=status.HTTP_201_CREATED
)
async def crear_instalacion(nueva: InstalacionCrear):
    return await crud.crear_instalacion(nueva)



@router.get(
    "/",
    response_model=List[Instalacion],
    status_code=status.HTTP_200_OK
)
async def listar_instalaciones():
    return await crud.listar_instalaciones()



@router.get(
    "/{instalacion_id}",
    response_model=Instalacion,
    status_code=status.HTTP_200_OK
)
async def obtener_instalacion(instalacion_id: str):
    return await crud.obtener_instalacion_por_id(instalacion_id)



@router.put(
    "/{instalacion_id}",
    response_model=Instalacion,
    status_code=status.HTTP_200_OK
)
async def actualizar_instalacion(instalacion_id: str, datos: InstalacionActualizar):
    return await crud.actualizar_instalacion(instalacion_id, datos)



@router.delete(
    "/{instalacion_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def eliminar_instalacion(instalacion_id: str):
    await crud.eliminar_instalacion(instalacion_id)
    return None
