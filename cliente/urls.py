from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from cliente.views import ClienteView, EquipoView

cliente_router = SimpleRouter()
cliente_router.register('clientes', ClienteView)

equipo_router = routers.NestedSimpleRouter(cliente_router, r'clientes', lookup='cliente')
equipo_router.register(r'equipos', EquipoView, basename='equipos')

