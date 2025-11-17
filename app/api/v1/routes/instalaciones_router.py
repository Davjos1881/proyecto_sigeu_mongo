from fastapi import APIRouter, status
from typing import List
from app.schemas.instalacion_schema import Instalacion, InstalacionCrear, InstalacionActualizar
from app.crud import instalaciones_crud

router = APIRouter()

@router.post("/", response_model=Instalacion, status_code=status.HTTP_201_CREATED)
async def crear_instalacion(data: InstalacionCrear):
    return await instalaciones_crud.crear_instalacion(data)

@router.get("/{instalacion_id}", response_model=Instalacion, status_code=status.HTTP_200_OK)
async def obtener_instalacion_por_id(instalacion_id: str):
    return await instalaciones_crud.obtener_instalacion_por_id(instalacion_id)

@router.get("/", response_model=List[Instalacion], status_code=status.HTTP_200_OK)
async def listar_instalaciones():
    return await instalaciones_crud.listar_instalaciones()

@router.put("/{instalacion_id}", response_model=Instalacion, status_code=status.HTTP_200_OK)
async def actualizar_instalacion(instalacion_id: str, data: InstalacionActualizar):
    return await instalaciones_crud.actualizar_instalacion(instalacion_id, data)

@router.delete("/{instalacion_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_instalacion(instalacion_id: str):
    await instalaciones_crud.eliminar_instalacion(instalacion_id)
    return None