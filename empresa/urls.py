from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from empresa.views import EmpresaView, ResponsableView

empresa_router = SimpleRouter()
empresa_router.register('empresas', EmpresaView)

empresa_nested_router = routers.NestedSimpleRouter(empresa_router, r'empresas', lookup='empresa')
empresa_nested_router.register(r'responsables', ResponsableView, basename='responsables')
