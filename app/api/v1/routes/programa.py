from fastapi import APIRouter, status
from typing import List

from app.schemas.programa import ProgramaCrear, Programa, ProgramaActualizar
from app.crud import programa_crud as crud

router = APIRouter()


@router.post("/", response_model=Programa, status_code=status.HTTP_201_CREATED)
async def crear_programa(nuevo: ProgramaCrear):
    return await crud.crear_programa(nuevo)


@router.get("/", response_model=List[Programa], status_code=status.HTTP_200_OK)
async def listar_programas():
    return await crud.listar_programas()


@router.get("/{programa_id}", response_model=Programa, status_code=status.HTTP_200_OK)
async def obtener_programa(programa_id: str):
    return await crud.obtener_programa_por_id(programa_id)


@router.put("/{programa_id}", response_model=Programa, status_code=status.HTTP_200_OK)
async def actualizar_programa(programa_id: str, datos: ProgramaActualizar):
    return await crud.actualizar_programa(programa_id, datos)


@router.delete("/{programa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_programa(programa_id: str):
    await crud.eliminar_programa(programa_id)
    return None
