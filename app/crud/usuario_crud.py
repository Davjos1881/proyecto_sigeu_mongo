from fastapi import HTTPException, status
from beanie import PydanticObjectId
from typing import List
from app.models.usuario import UsuarioModel
from app.schemas.usuario_schema import UsuarioCrear, Usuario, UsuarioActualizar
from bson import ObjectId

async def crear_usuario(nuevo_usuario: UsuarioCrear) -> Usuario:
    usuario = UsuarioModel(**nuevo_usuario.model_dump())
    await usuario.insert()

    data = nuevo_usuario.model_dump()
    return Usuario(id=str(usuario.id), **data)


async def obtener_usuario_por_id(usuario_id: str) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )

    user = await UsuarioModel.get(object_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario {usuario_id} no encontrado"
        )

    data = user.model_dump()
    data.pop("id", None)  # ID lo pasamos manualmente

    # ---------------------------------------------------------
    # 🔧 CORRECCIÓN DE ObjectId ANIDADOS QUE ROMPEN PYDANTIC
    # ---------------------------------------------------------

    # Convertir perfil.estudiante.programa_id → str
    if "perfil" in data and isinstance(data["perfil"], dict):
        perfil = data["perfil"]

        if "estudiante" in perfil and isinstance(perfil["estudiante"], dict):
            est = perfil["estudiante"]

            if "programa_id" in est and isinstance(est["programa_id"], ObjectId):
                est["programa_id"] = str(est["programa_id"])

    # Convertir notificaciones → lista de dicts
    if "notificaciones" in data and isinstance(data["notificaciones"], list):
        for notif in data["notificaciones"]:
            if isinstance(notif.get("id_notificacion"), ObjectId):
                notif["id_notificacion"] = str(notif["id_notificacion"])

            if isinstance(notif.get("evento_id"), ObjectId):
                notif["evento_id"] = str(notif["evento_id"])

    # ---------------------------------------------------------

    return Usuario(id=str(user.id), **data)


async def listar_usuarios():
    usuarios = await UsuarioModel.find_all().to_list()
    usuarios_limpios = []

    for u in usuarios:
        data = u.model_dump()
        
        # Convertir ID principal
        data["id"] = str(u.id)

        # -------------------------
        #   NORMALIZAR PERFILES
        # -------------------------
        if data.get("perfil"):

            est = data["perfil"].get("estudiante")
            if est and est.get("programa_id"):
                est["programa_id"] = str(est["programa_id"])

            doc = data["perfil"].get("docente")
            if doc and doc.get("unidad_id"):
                doc["unidad_id"] = str(doc["unidad_id"])

        # -------------------------
        #   NORMALIZAR NOTIFICACIONES
        # -------------------------
        notificaciones = data.get("notificaciones", [])
        for n in notificaciones:
            if n.get("id_notificacion"):
                n["id_notificacion"] = str(n["id_notificacion"])
            if n.get("evento_id"):
                n["evento_id"] = str(n["evento_id"])

        usuarios_limpios.append(Usuario(**data))

    return usuarios_limpios

async def actualizar_usuario(usuario_id: str, datos: UsuarioActualizar) -> Usuario:
    try:
        object_id = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )

    user = await UsuarioModel.get(object_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario {usuario_id} no encontrado"
        )

    updates = datos.model_dump(exclude_unset=True)
    for k, v in updates.items():
        setattr(user, k, v)

    await user.save()

    data = user.model_dump()
    data.pop("id", None)

    return Usuario(id=str(user.id), **data)


async def eliminar_usuario(usuario_id: str) -> None:
    try:
        oid = PydanticObjectId(usuario_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )

    user = await UsuarioModel.get(oid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario {usuario_id} no encontrado"
        )

    await user.delete()
    return None