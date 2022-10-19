from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from .views import CargoView, TrabajadorView

trabajador_router = SimpleRouter()
trabajador_router.register('trabajadores', TrabajadorView)
trabajador_router.register('cargos', CargoView)

