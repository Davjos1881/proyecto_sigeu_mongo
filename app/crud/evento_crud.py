from fastapi import HTTPException, status
from app.models.evento import EventoModel
from app.schemas.evento_schema import EventoCrear, Evento, EventoActualizar
from beanie import PydanticObjectId
from typing import List, Dict, Any


def objectid_to_str(obj):
    if obj is None:
        return None
    obj_dict = obj.model_dump(exclude={"id"})
    for field_name, value in obj_dict.items():
        if isinstance(value, PydanticObjectId):
            obj_dict[field_name] = str(value)
        elif isinstance(value, list):
            new_list = []
            for item in value:
                if hasattr(item, "model_dump"):
                    new_list.append(objectid_to_str(item))
                else:
                    new_list.append(item)
            obj_dict[field_name] = new_list
        elif hasattr(value, "model_dump"):
            obj_dict[field_name] = objectid_to_str(value)
    return obj_dict


async def listar_eventos() -> List[Evento]:
    eventos = await EventoModel.find_all().to_list()
    resultados = []
    for e in eventos:
        datos = objectid_to_str(e)
        resultados.append(Evento(id=str(e.id), **datos))
    return resultados


async def crear_evento(nuevo_evento: EventoCrear) -> Evento:
    ev = EventoModel(**nuevo_evento.model_dump())
    await ev.insert()
    datos = objectid_to_str(ev)
    return Evento(id=str(ev.id), **datos)


async def obtener_evento_por_id(evento_id: str) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")
    datos = objectid_to_str(ev)
    return Evento(id=str(ev.id), **datos)


async def actualizar_evento(evento_id: str, datos: EventoActualizar) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")

    campos_actualizados = datos.model_dump(exclude_unset=True)
    for k, v in campos_actualizados.items():
        setattr(ev, k, v)
    await ev.save()
    datos_final = objectid_to_str(ev)
    return Evento(id=str(ev.id), **datos_final)


async def eliminar_evento(evento_id: str) -> None:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    ev = await EventoModel.get(object_id)
    if not ev:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Evento {evento_id} no encontrado")
    await ev.delete()



async def agregar_revision(evento_id: str, revision: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"revisiones": revision}})
    return await obtener_evento_por_id(evento_id)


async def actualizar_revision(evento_id: str, id_revision: Any, changes: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    set_ops = {f"revisiones.$.{k}": v for k, v in changes.items()}
    await EventoModel.find_one({"_id": object_id, "revisiones.id_revision": id_revision}).update({"$set": set_ops})
    return await obtener_evento_por_id(evento_id)


async def agregar_aval(evento_id: str, aval: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"avales": aval}})
    return await obtener_evento_por_id(evento_id)


async def eliminar_aval(evento_id: str, id_aval: Any) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$pull": {"avales": {"id_aval": id_aval}}})
    return await obtener_evento_por_id(evento_id)


async def agregar_responsable(evento_id: str, responsable: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$push": {"responsables": responsable}})
    return await obtener_evento_por_id(evento_id)


async def eliminar_responsable(evento_id: str, usuario_id: Any) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$pull": {"responsables": {"usuario_id": usuario_id}}})
    return await obtener_evento_por_id(evento_id)


async def agregar_certificado_participacion(evento_id: str, certificado_meta: Dict[str, Any]) -> Evento:
    try:
        object_id = PydanticObjectId(evento_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id de evento invalido")
    await EventoModel.find_one({"_id": object_id}).update({"$set": {"certificado_participacion": certificado_meta}})
    return await obtener_evento_por_id(evento_id)