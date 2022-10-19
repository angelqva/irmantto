from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from helpers.helper import NestedViewSetMixin
from empresa.serializers import *
from user.serializers import MediumUserSerializer, UserSerializer


class EmpresaView(NestedViewSetMixin):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    read_serializer_class = EmpresaReadSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=["post"], detail=True, url_path="crear-usuario", serializer_class=MediumUserSerializer)
    def crear_usuario(self, request, **kwargs):
        empresa = self.get_object()
        if empresa.usuario is not None:
            raise ValidationError({"empresa": [f"{str(empresa)} ya tiene el usuario: {str(empresa.usuario)}"]})
        data: dict = request.data
        data["rol"] = 'Empresa'
        data["is_superuser"] = False
        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid(raise_exception=True)
        instance = user_serializer.save()
        empresa.usuario = instance
        empresa.save()
        return_data = MediumUserSerializer(instance=instance).data
        return Response(return_data, status=status.HTTP_201_CREATED)

    @action(methods=["delete"], detail=True, url_path="eliminar-usuario")
    def eliminar_usuario(self, request, **kwargs):
        empresa = self.get_object()
        usuario = empresa.usuario
        if usuario is None:
            raise ValidationError({"empresa": [f"{str(empresa)} no tiene usuario en el sistema"]})
        usuario.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ResponsableView(NestedViewSetMixin):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableSerializer
    read_serializer_class = ClienteReadSerializer
    permission_classes = (IsAuthenticated,)
