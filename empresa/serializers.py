from rest_framework import serializers
from rest_framework.validators import ValidationError
from empresa.models import Empresa, Responsable
from cliente.serializers import ClienteReadSerializer
from user.serializers import MediumUserSerializer


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('id', 'carnet_identidad', 'nombre', 'apellidos', 'direccion', 'telefono')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data, **kwargs):
        kwargs: dict = self.context["view"].kwargs
        empresa_pk = kwargs['empresa_pk']
        try:
            empresa = Empresa.objects.get(pk=empresa_pk)
            validated_data["empresa"] = empresa
        except Empresa.DoesNotExist:
            raise ValidationError({"empresa_pk": [f"cliente_pk:{empresa_pk} no esta en la base de datos"]})
        return Responsable.objects.create(**validated_data)


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'nombre', 'direccion', 'registro', 'telefono')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class EmpresaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('nombre', 'direccion', 'registro', 'telefono', 'usuario', 'responsables')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    usuario = MediumUserSerializer()
    responsables = ClienteReadSerializer(many=True)


