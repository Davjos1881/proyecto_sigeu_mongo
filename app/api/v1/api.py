from fastapi import APIRouter

from app.api.v1.routes import usuarios_router, programas_router, unidades_router, organizaciones_router, instalaciones_router, facultades_router, evento_router

# Crea un enrutador principal para la v1
api_router_v1 = APIRouter()


# Routers añadidos
api_router_v1.include_router(usuarios_router.router, prefix="/usuarios", tags=["Usuarios"])
api_router_v1.include_router(programas_router.router, prefix="/programas", tags=["Programas"])
api_router_v1.include_router(unidades_router.router, prefix="/unidades", tags=["Unidades"])
api_router_v1.include_router(organizaciones_router.router, prefix="/organizaciones", tags=["Organizaciones"])
api_router_v1.include_router(instalaciones_router.router, prefix="/instalaciones", tags=["Instalaciones"])
api_router_v1.include_router(facultades_router.router, prefix="/facultades", tags=["Facultades"])
api_router_v1.include_router(evento_router.router)

