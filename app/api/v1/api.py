from fastapi import APIRouter

from app.api.v1.routes import paciente, programas_router, usuarios_router, facultades_router, evento_router, instalaciones_router, unidades_router, organizaciones_router

# Crea un enrutador principal para la v1
api_router_v1 = APIRouter()

api_router_v1.include_router(paciente.router, prefix="/pacientes", tags=["Pacientes"])

api_router_v1.include_router(usuarios_router.router, prefix="/usuarios")
api_router_v1.include_router(programas_router.router, prefix="/programas")
api_router_v1.include_router(facultades_router.router, prefix="/facultades")
api_router_v1.include_router(evento_router.router, prefix="/eventos")
api_router_v1.include_router(instalaciones_router.router, prefix="/instalaciones")
api_router_v1.include_router(unidades_router.router, prefix="/unidades")
api_router_v1.include_router(organizaciones_router.router, prefix="/organizaciones")

