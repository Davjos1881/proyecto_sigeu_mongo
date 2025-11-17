from fastapi import APIRouter, status
from typing import List
from app.schemas.facultad_schema import Facultad, FacultadCrear, FacultadActualizar
from app.crud import facultad_crud

router = APIRouter()

@router.post("/", response_model=Facultad, status_code=status.HTTP_201_CREATED)
async def crear_facultad(data: FacultadCrear):
    return await facultad_crud.crear_facultad(data)

@router.get("/{facultad_id}", response_model=Facultad, status_code=status.HTTP_200_OK)
async def obtener_facultad(facultad_id: str):
    return await facultad_crud.obtener_facultad_por_id(facultad_id)

@router.get("/", response_model=List[Facultad], status_code=status.HTTP_200_OK)
async def listar_facultades():
    return await facultad_crud.listar_facultades()

@router.put("/{facultad_id}", response_model=Facultad, status_code=status.HTTP_200_OK)
async def actualizar_facultad(facultad_id: str, data: FacultadActualizar):
    return await facultad_crud.actualizar_facultad(facultad_id, data)

@router.delete("/{facultad_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_facultad(facultad_id: str):
    await facultad_crud.eliminar_facultad(facultad_id)
    return None
