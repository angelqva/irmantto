from rest_framework.permissions import IsAuthenticated
from helpers.helper import NestedViewSetMixin
from cliente.serializers import *
from solicitud.serializers import Solicitud, SolicitudSerializer, SolicitudReadSerializer


class SolicitudView(NestedViewSetMixin):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    read_serializer_class = SolicitudReadSerializer
    permission_classes = (IsAuthenticated,)
