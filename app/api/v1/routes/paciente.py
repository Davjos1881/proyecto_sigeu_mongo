from fastapi import APIRouter, status
from typing import List

from app.schemas.paciente import PacienteCrear, Paciente, PacienteActualizar
from app.crud import paciente as crud

router = APIRouter()

@router.post("/", response_model=Paciente, status_code=status.HTTP_201_CREATED)
async def crear_paciente(nuevo_paciente: PacienteCrear):
    return await crud.crear_paciente(nuevo_paciente)


@router.get("/", response_model=List[Paciente], status_code=status.HTTP_200_OK)
async def listar_pacientes():
    return await crud.listar_pacientes()


@router.get("/{paciente_id}", response_model=Paciente, status_code=status.HTTP_200_OK)
async def obtener_paciente(paciente_id: str):
    return await crud.obtener_paciente_por_id(paciente_id)


@router.put("/{paciente_id}", response_model=Paciente, status_code=status.HTTP_200_OK)
async def actualizar_paciente(paciente_id: str, datos_actualizados: PacienteActualizar):
    return await crud.actualizar_paciente(paciente_id, datos_actualizados)


@router.get("/{paciente_id}/padres", status_code=status.HTTP_200_OK)
async def buscar_padres_paciente(paciente_id: str):
    """
    Retorna los contactos de emergencia del tipo 'padre' o 'madre'.
    """
    return await crud.buscar_padres_paciente(paciente_id)
