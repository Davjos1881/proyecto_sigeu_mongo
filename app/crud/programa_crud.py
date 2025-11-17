from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List
from app.models.programa import ProgramaModel
from app.schemas.programa_schema import ProgramaCrear, Programa, ProgramaActualizar


async def crear_programa(nuevo: ProgramaCrear) -> Programa:
    p = ProgramaModel(**nuevo.model_dump())
    await p.insert()

    data = p.model_dump()
    data["id"] = str(p.id)
    return Programa(**data)


async def obtener_programa_por_id(programa_id: str) -> Programa:
    try:
        object_id = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="id de programa inválido")
    p = await ProgramaModel.get(object_id)
    if not p:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Programa {programa_id} no encontrado"
        )

    data = p.model_dump()
    data["id"] = str(p.id)
    return Programa(**data)


async def listar_programas() -> List[Programa]:
    items = await ProgramaModel.find_all().to_list()

    resultado = []
    for x in items:
        data = x.model_dump()
        data["id"] = str(x.id)
        resultado.append(Programa(**data))

    return resultado


async def actualizar_programa(programa_id: str, datos: ProgramaActualizar) -> Programa:
    try:
        object_id = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id de programa inválido"
        )
 
    p = await ProgramaModel.get(object_id)
    if not p:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Programa {programa_id} no encontrado"
        )

    if datos.nombre_programa is not None:
        p.nombre_programa = datos.nombre_programa

    if datos.facultad is not None:

        if datos.facultad.id_facultad is not None:
            try:
                datos.facultad.id_facultad = PydanticObjectId(datos.facultad.id_facultad)
            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="id_facultad inválido"
                )

        p.facultad = datos.facultad

    await p.save()

    data = p.model_dump()
    data["id"] = str(p.id)

    return Programa(**data)


async def eliminar_programa(programa_id: str) -> None:
    try:
        oid = PydanticObjectId(programa_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id de programa inválido"
        )

    p = await ProgramaModel.get(oid)
    if not p:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Programa {programa_id} no encontrado"
        )

    await p.delete()
    return None