from rest_framework.routers import SimpleRouter
from .views import TareaView

tarea_router = SimpleRouter()
tarea_router.register('tareas', TareaView, basename='tareas')
