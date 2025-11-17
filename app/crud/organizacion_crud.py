from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List, Optional
from app.models.organizacion import OrganizacionExternaModel
from app.schemas.organizacion_schema import OrganizacionCrear, Organizacion, OrganizacionActualizar

async def crear_organizacion(nuevo: OrganizacionCrear) -> Organizacion:
    org = OrganizacionExternaModel(**nuevo.model_dump())
    await org.insert()
    data = nuevo.model_dump()
    data.pop("id", None)  # evitar conflicto con id
    return Organizacion(id=str(org.id), **data)

async def obtener_organizacion_por_id(org_id: str) -> Organizacion:
    try:
        object_id = PydanticObjectId(org_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de organización inválido")
    
    org = await OrganizacionExternaModel.get(object_id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organización {org_id} no encontrada")
    
    data = org.model_dump()
    data.pop("id", None)  # evitar conflicto con id
    return Organizacion(id=str(org.id), **data)

async def listar_organizaciones(q: Optional[str] = None) -> List[Organizacion]:
    if q:
        items = await OrganizacionExternaModel.find(
            {"nombre_organizacion": {"$regex": q, "$options": "i"}}
        ).to_list()
    else:
        items = await OrganizacionExternaModel.find_all().to_list()

    return [
        Organizacion(
            id=str(org.id),
            nombre_organizacion=org.nombre_organizacion,
            representante_legal=org.representante_legal,
            telefono=org.telefono,
            direccion=org.direccion,
            actividad=org.actividad,
            sector_economico=org.sector_economico,
        )
        for org in items
    ]

async def actualizar_organizacion(org_id: str, datos: OrganizacionActualizar) -> Organizacion:
    try:
        object_id = PydanticObjectId(org_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de organización inválido")

    org = await OrganizacionExternaModel.get(object_id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organización {org_id} no encontrada")

    org.nombre_organizacion = datos.nombre_organizacion or org.nombre_organizacion
    org.representante_legal = datos.representante_legal or org.representante_legal
    org.telefono = datos.telefono or org.telefono
    org.direccion = datos.direccion or org.direccion
    org.actividad = datos.actividad or org.actividad
    org.sector_economico = datos.sector_economico or org.sector_economico

    await org.save()

    data = org.model_dump()
    data.pop("id", None)  # evitar conflicto con id
    return Organizacion(id=str(org.id), **data)

async def eliminar_organizacion(org_id: str) -> None:
    try:
        object_id = PydanticObjectId(org_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de organización inválido")
    
    org = await OrganizacionExternaModel.get(object_id)
    if not org:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organización {org_id} no encontrada")
    
    await org.delete()
    return None