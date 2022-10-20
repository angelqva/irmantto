from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from .views import SolicitudView

solicitud_router = SimpleRouter()
solicitud_router.register('solicitudes', SolicitudView)
