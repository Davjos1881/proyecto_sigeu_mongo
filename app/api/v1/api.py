from fastapi import APIRouter

# Importa el enrutador específico del módulo de pacientes
from app.api.v1.routes import paciente
from app.api.v1.routes import usuario
from app.api.v1.routes import programa
from app.api.v1.routes import unidad
from app.api.v1.routes import organizacion
from app.api.v1.routes import instalacion
from app.api.v1.routes import facultad
from app.api.v1.routes import evento

# Crea un enrutador principal para la v1
api_router_v1 = APIRouter()

# Incluye el enrutador de pacientes bajo el prefijo /pacientes
# Todas las rutas en paciente.router ahora comenzarán con /pacientes
# y estarán agrupadas bajo la etiqueta "Pacientes" en la documentación.
api_router_v1.include_router(paciente.router, prefix="/pacientes", tags=["Pacientes"])

# Routers añadidos
api_router_v1.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
api_router_v1.include_router(programa.router, prefix="/programas", tags=["Programas"])
api_router_v1.include_router(unidad.router, prefix="/unidades", tags=["Unidades"])
api_router_v1.include_router(organizacion.router, prefix="/organizaciones", tags=["Organizaciones"])
api_router_v1.include_router(instalacion.router, prefix="/instalaciones", tags=["Instalaciones"])
api_router_v1.include_router(facultad.router, prefix="/facultades", tags=["Facultades"])
api_router_v1.include_router(evento.router, prefix="/eventos", tags=["Eventos"])

# Si en el futuro tienes un enrutador para "Doctores", lo agregarías aquí:
# from app.api.v1.routes import doctor
# api_router_v1.include_router(doctor.router, prefix="/doctores", tags=["Doctores"])
