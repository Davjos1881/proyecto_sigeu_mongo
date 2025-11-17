from fastapi import APIRouter, status
from typing import List
from app.schemas.unidad_schema import Unidad, UnidadCrear, UnidadActualizar
from app.crud import unidades_crud

router = APIRouter()

@router.post("/", response_model=Unidad, status_code=status.HTTP_201_CREATED)
async def crear_unidad(data: UnidadCrear):
    return await unidades_crud.crear_unidad(data)

@router.get("/{unidad_id}", response_model=Unidad, status_code=status.HTTP_200_OK)
async def obtener_unidad(unidad_id: str):
    return await unidades_crud.obtener_unidad_por_id(unidad_id)

@router.get("/", response_model=List[Unidad], status_code=status.HTTP_200_OK)
async def listar_unidades():
    return await unidades_crud.listar_unidades()

@router.put("/{unidad_id}", response_model=Unidad, status_code=status.HTTP_200_OK)
async def actualizar_unidad(unidad_id: str, data: UnidadActualizar):
    return await unidades_crud.actualizar_unidad(unidad_id, data)

@router.delete("/{unidad_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_unidad(unidad_id: str):
    await unidades_crud.eliminar_unidad(unidad_id)
    return None