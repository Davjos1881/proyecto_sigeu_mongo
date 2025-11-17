from fastapi import APIRouter, status
from typing import List
from app.schemas.programa_schema import Programa, ProgramaCrear, ProgramaActualizar
from app.crud import programa_crud

router = APIRouter()

@router.post("/", response_model=Programa, status_code=status.HTTP_201_CREATED)
async def crear_programa(data: ProgramaCrear):
    return await programa_crud.crear_programa(data)

@router.get("/{programa_id}", response_model=Programa, status_code=status.HTTP_200_OK)
async def obtener_programa(programa_id: str):
    return await programa_crud.obtener_programa_por_id(programa_id)

@router.get("/", response_model=List[Programa], status_code=status.HTTP_200_OK)
async def listar_programas():
    return await programa_crud.listar_programas()

@router.put("/{programa_id}", response_model=Programa, status_code=status.HTTP_200_OK)
async def actualizar_programa(programa_id: str, data: ProgramaActualizar):
    return await programa_crud.actualizar_programa(programa_id, data)

@router.delete("/{programa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_programa(programa_id: str):
    await programa_crud.eliminar_programa(programa_id)
    return None