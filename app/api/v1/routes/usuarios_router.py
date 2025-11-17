from fastapi import APIRouter, status
from typing import List, Optional
from app.schemas.usuario_schema import Usuario, UsuarioCrear, UsuarioActualizar
from app.crud import usuario_crud

router = APIRouter()

@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def crear_usuario(data: UsuarioCrear):
    return await usuario_crud.crear_usuario(data)

@router.get("/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def obtener_usuario(usuario_id: str):
    return await usuario_crud.obtener_usuario_por_id(usuario_id)

@router.get("/", response_model=List[Usuario], status_code=status.HTTP_200_OK)
async def listar_usuarios():
    return await usuario_crud.listar_usuarios()

@router.put("/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def actualizar_usuario(usuario_id: str, data: UsuarioActualizar):
    return await usuario_crud.actualizar_usuario(usuario_id, data)

@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(usuario_id: str):
    await usuario_crud.eliminar_usuario(usuario_id)
    return None