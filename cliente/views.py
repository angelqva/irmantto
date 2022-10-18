from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from helpers.helper import NestedViewSetMixin
from user.serializers import UserSerializer
from cliente.serializers import *


class ClienteView(NestedViewSetMixin):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    read_serializer_class = ClienteReadSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["post"], detail=True, url_path="crear-usuario", serializer_class=ClienteUserSerializer)
    def crear_usuario(self, request, **kwargs):
        cliente = self.get_object()
        if cliente.usuario is not None:
            raise ValidationError({"cliente": [f"{str(cliente)} ya tiene el usuario: {str(cliente.usuario)}"]})
        data: dict = request.data
        data["name"] = cliente.nombre
        data["lastname"] = cliente.apellidos
        data["rol"] = 'Cliente'
        data["is_superuser"] = False
        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        instance = user_serializer.save()
        cliente.usuario = instance
        cliente.save()
        return_data = ClienteUserSerializer(instance=instance).data
        return Response(return_data, status=status.HTTP_201_CREATED)

    @action(methods=["delete"], detail=True, url_path="eliminar-usuario")
    def eliminar_usuario(self, request, **kwargs):
        cliente = self.get_object()
        usuario = cliente.usuario
        if usuario is None:
            raise ValidationError({"cliente": [f"{str(cliente)} no tiene usuario en el sistema"]})
        usuario.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class EquipoView(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().select_related(
        'cliente'
    )
    serializer_class = EquipoSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        cliente_id = self.kwargs.get("cliente_pk")
        if cliente_id is not None:
            try:
                cliente = Cliente.objects.get(pk=cliente_id)
            except Cliente.DoesNotExist:
                raise NotFound('Cliente not found')
            return self.queryset.filter(cliente=cliente)

        return self.queryset
