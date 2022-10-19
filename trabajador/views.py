from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.validators import ValidationError
from helpers.helper import NestedViewSetMixin
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
from .serializers import *


class CargoView(viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Cargo.objects.all().prefetch_related('trabajadores',
                                                    'trabajadores__usuario',
                                                    'trabajadores__jefe_equipo',
                                                    'trabajadores__jefe_equipo__usuario'
                                                    'trabajadores__jefe_equipo__cargo')


class TrabajadorView(NestedViewSetMixin):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer
    read_serializer_class = TrabajadorReadSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["post"], detail=True, url_path="crear-usuario", serializer_class=SimpleUserSerializer)
    def crear_usuario(self, request, **kwargs):
        trabajador = self.get_object()
        if trabajador.usuario is not None:
            raise ValidationError({"trabajador": [f"{str(trabajador)} ya tiene el usuario: {str(trabajador.usuario)}"]})
        data: dict = request.data
        data["name"] = trabajador.nombre
        data["lastname"] = trabajador.apellidos
        data["rol"] = 'Trabajador'
        data["is_superuser"] = False
        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        instance = user_serializer.save()
        trabajador.usuario = instance
        trabajador.save()
        return_data = SimpleUserSerializer(instance=instance).data
        return Response(return_data, status=status.HTTP_201_CREATED)

    @action(methods=["delete"], detail=True, url_path="eliminar-usuario")
    def eliminar_usuario(self, request, **kwargs):
        trabajador = self.get_object()
        usuario = trabajador.usuario
        if usuario is None:
            raise ValidationError({"trabajador": [f"{str(trabajador)} no tiene usuario en el sistema"]})
        usuario.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
