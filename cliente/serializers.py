from rest_framework import serializers
from rest_framework.validators import ValidationError
from user.models import User
from .models import (
    Cliente,
    Equipo
)


class EquipoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'marca', 'ubicacion')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        kwargs: dict = self.context["view"].kwargs
        cliente_id = kwargs['cliente_pk']
        cliente = Cliente.objects.get(pk=cliente_id)
        cantidad = cliente.equipos.filter(nombre=validated_data["nombre"]).count()
        if cantidad > 0:
            raise ValidationError(
                {"nombre": [f"{cliente.nombre} ya tiene el equipo con nombre {validated_data['nombre']}"]}
            )
        validated_data["cliente"] = cliente
        return Equipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        kwargs: dict = self.context["view"].kwargs
        if instance.nombre != validated_data["nombre"]:
            cliente_id = kwargs['cliente_pk']
            cliente = Cliente.objects.get(pk=cliente_id)
            cantidad = cliente.equipos.filter(nombre=validated_data["nombre"]).count()
            if cantidad > 0:
                raise ValidationError(
                    {"nombre": [f"Cliente({cliente.nombre}) ya tiene el equipo con nombre {validated_data['nombre']}"]}
                )
        return super().update(instance, validated_data)


class ClienteUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'read_only': True},
            'username': {'read_only': True},
        }


class ClienteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }


class ClienteEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'marca', 'ubicacion')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellidos', 'direccion', 'telefono')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ClienteReadSerializer(serializers.ModelSerializer):
    usuario = ClienteUserReadSerializer()
    equipos = ClienteEquipoSerializer(many=True)

    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellidos', 'direccion', 'telefono', 'equipos', 'usuario')
        extra_kwargs = {
            'id': {'read_only': True},
        }
