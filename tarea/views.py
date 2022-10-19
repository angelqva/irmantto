from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import Tarea, TareaSerializer


class TareaView(ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
    permission_classes = (IsAuthenticated,)
