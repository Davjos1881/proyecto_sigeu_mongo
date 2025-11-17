from fastapi import APIRouter, Query, status
from typing import List, Optional
from app.schemas.organizacion_schema import Organizacion, OrganizacionCrear, OrganizacionActualizar
from app.crud import organizacion_crud

router = APIRouter()

@router.post("/", response_model=Organizacion, status_code=status.HTTP_201_CREATED)
async def crear_organizacion(data: OrganizacionCrear):
    return await organizacion_crud.crear_organizacion(data)

@router.get("/{org_id}", response_model=Organizacion, status_code=status.HTTP_200_OK)
async def obtener_organizacion(org_id: str):
    return await organizacion_crud.obtener_organizacion_por_id(org_id)

@router.get("/", response_model=List[Organizacion], status_code=status.HTTP_200_OK)
async def listar_organizaciones():
    return await organizacion_crud.listar_organizaciones()

@router.put("/{org_id}", response_model=Organizacion, status_code=status.HTTP_200_OK)
async def actualizar_organizacion(org_id: str, data: OrganizacionActualizar):
    return await organizacion_crud.actualizar_organizacion(org_id, data)

@router.delete("/{org_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_organizacion(org_id: str):
    await organizacion_crud.eliminar_organizacion(org_id)
    return None