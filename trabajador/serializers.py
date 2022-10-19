from rest_framework import serializers
from .models import *
from user.serializers import SimpleUserSerializer


class SimpleCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class JefeTrabajadorSerializer(serializers.ModelSerializer):
    cargo = SimpleCargoSerializer(many=False, read_only=True)
    usuario = SimpleUserSerializer()

    class Meta:
        model = Trabajador
        fields = ('id', 'carnet_identidad', 'nombre', 'apellidos', 'direccion',
                  'telefono', 'escolaridad', 'categoria', 'cargo', 'usuario')


class SimpleTrabajadorSerializer(serializers.ModelSerializer):
    jefe_equipo = JefeTrabajadorSerializer(many=False, read_only=True)
    usuario = SimpleUserSerializer()

    class Meta:
        model = Trabajador
        fields = ('id', 'carnet_identidad', 'nombre', 'apellidos', 'direccion',
                  'telefono', 'escolaridad', 'categoria', 'jefe_equipo', 'usuario')


class CargoSerializer(serializers.ModelSerializer):
    trabajadores = SimpleTrabajadorSerializer(many=True, read_only=True)

    class Meta:
        model = Cargo
        fields = ('id', 'nombre', 'descripcion', 'trabajadores')


class TrabajadorSerializer(serializers.ModelSerializer):
    cargo = serializers.PrimaryKeyRelatedField(
        queryset=Cargo.objects.all(), required=False,
        allow_null=True)
    jefe_equipo = serializers.PrimaryKeyRelatedField(
        required=False, allow_null=True,
        label="Jefe de Equipo", queryset=Trabajador.objects.all(),
    )

    class Meta:
        model = Trabajador
        fields = ('id', 'carnet_identidad', 'nombre', 'apellidos',  'direccion', 'telefono',
                  'escolaridad', 'categoria', 'cargo', 'jefe_equipo')

        extra_kwargs = {
            'id': {'read_only': True},
        }


class TrabajadorReadSerializer(serializers.ModelSerializer):
    cargo = SimpleCargoSerializer(many=False)
    jefe_equipo = JefeTrabajadorSerializer()
    usuario = SimpleUserSerializer()

    class Meta:
        model = Trabajador
        fields = ('id', 'carnet_identidad', 'nombre', 'apellidos', 'direccion', 'telefono',
                  'escolaridad', 'categoria', 'cargo', 'jefe_equipo', 'usuario')

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'rol': {'read_only': True},
        }
