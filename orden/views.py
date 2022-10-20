from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from helpers.helper import NestedViewSetMixin
from .serializer import OrdenSerializer, OrdenReadSerializer, Orden, TareaOrdenSerializer, TareaOrden


class OrdenView(NestedViewSetMixin):
    serializer_class = OrdenSerializer
    read_serializer_class = OrdenReadSerializer
    queryset = Orden.objects.all()
    permission_classes = (IsAuthenticated,)


class TareaOrdenView(viewsets.ModelViewSet):
    serializer_class = TareaOrdenSerializer
    queryset = TareaOrden.objects.all()
    permission_classes = (IsAuthenticated,)
    