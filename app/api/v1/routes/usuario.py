from fastapi import APIRouter, status
from typing import List

from app.schemas.usuario import UsuarioCrear, Usuario, UsuarioActualizar
from app.crud import usuario_crud as crud

router = APIRouter()


@router.post("/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
async def crear_usuario(nuevo_usuario: UsuarioCrear):
    return await crud.crear_usuario(nuevo_usuario)


@router.get("/", response_model=List[Usuario], status_code=status.HTTP_200_OK)
async def listar_usuarios():
    return await crud.listar_usuarios()


@router.get("/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def obtener_usuario(usuario_id: str):
    return await crud.obtener_usuario_por_id(usuario_id)


@router.put("/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def actualizar_usuario(usuario_id: str, datos: UsuarioActualizar):
    return await crud.actualizar_usuario(usuario_id, datos)


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_usuario(usuario_id: str):
    await crud.eliminar_usuario(usuario_id)
    return None
