from rest_framework.routers import SimpleRouter
from .views import OrdenView, TareaOrdenView

orden_router = SimpleRouter()
orden_router.register('ordenes', OrdenView)
orden_router.register('ordenes-tareas', TareaOrdenView)
