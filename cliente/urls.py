from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from cliente.views import ClienteView, EquipoView, SolicitudClienteView

cliente_router = SimpleRouter()
cliente_router.register('clientes', ClienteView)

cliente_nested_router = routers.NestedSimpleRouter(cliente_router, r'clientes', lookup='cliente')
cliente_nested_router.register(r'equipos', EquipoView, basename='equipos')
cliente_nested_router.register(r'solicitud-trabajo', SolicitudClienteView, basename='solicitud-trabajo')

