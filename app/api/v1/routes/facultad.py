from fastapi import APIRouter, status
from typing import List

from app.schemas.facultad import FacultadCrear, Facultad, FacultadActualizar
from app.crud import facultad_crud as crud

router = APIRouter()



@router.post(
    "/", 
    response_model=Facultad, 
    status_code=status.HTTP_201_CREATED
)
async def crear_facultad(nueva: FacultadCrear):
    return await crud.crear_facultad(nueva)



@router.get(
    "/", 
    response_model=List[Facultad], 
    status_code=status.HTTP_200_OK
)
async def listar_facultades():
    return await crud.listar_facultades()



@router.get(
    "/{facultad_id}", 
    response_model=Facultad, 
    status_code=status.HTTP_200_OK
)
async def obtener_facultad(facultad_id: str):
    return await crud.obtener_facultad_por_id(facultad_id)



@router.put(
    "/{facultad_id}", 
    response_model=Facultad, 
    status_code=status.HTTP_200_OK
)
async def actualizar_facultad(facultad_id: str, datos: FacultadActualizar):
    return await crud.actualizar_facultad(facultad_id, datos)



@router.delete(
    "/{facultad_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
async def eliminar_facultad(facultad_id: str):
    await crud.eliminar_facultad(facultad_id)
    return None
