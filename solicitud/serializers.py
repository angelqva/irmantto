from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Cliente, Equipo, Solicitud
from datetime import date
from cliente.serializers import ClienteSerializer, ClienteEquipoSerializer
from trabajador.serializers import JefeTrabajadorSerializer


class SolicitudClienteSerializers(serializers.ModelSerializer):
    equipos = serializers.PrimaryKeyRelatedField(many=True, queryset=Equipo.objects.all())
    fecha = serializers.DateField(default=date.today())

    class Meta:
        model = Solicitud
        fields = ('id', 'equipos', 'fecha')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data: dict):
        kwargs: dict = self.context["view"].kwargs
        cliente_id = kwargs['cliente_pk']
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            raise ValidationError({"cliente": [f"cliente_pk:{cliente_id} no esta en la base de datos"]})
        cantidad = Solicitud.objects.filter(fecha_creacion=date.today(), cliente_id=cliente.id).count()
        if cantidad > 0:
            raise ValidationError({
                "fecha_creacion": [
                    f"Solo esta permitido una solicitud por día",
                    f"Actualice la solicitud con fecha de creación: {date.today()}"
                ]
            })
        validated_data["cliente"] = cliente
        validated_data["jefe_equipo"] = None
        print(validated_data)
        return super().create(validated_data)

    def update(self, instance: Solicitud, validated_data: dict):
        kwargs: dict = self.context["view"].kwargs
        cliente_id = kwargs['cliente_pk']
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            raise ValidationError({"cliente": [f"cliente_pk:{cliente_id} no esta en la base de datos"]})
        validated_data["cliente"] = cliente
        return super().update(instance, validated_data)


class SolicitudClienteReadSerializers(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    equipos = ClienteEquipoSerializer(many=True)
    jefe_equipo = JefeTrabajadorSerializer()

    class Meta:
        model = Solicitud
        fields = '__all__'


class SolicitudSerializer(serializers.ModelSerializer):
    fecha = serializers.DateField(default=date.today())

    class Meta:
        model = Solicitud
        fields = '__all__'

    def create(self, validated_data):
        cliente = validated_data["cliente"]
        if cliente is not None:
            cantidad = Solicitud.objects.filter(fecha_creacion=date.today(), cliente_id=cliente.id).count()
            if cantidad > 0:
                raise ValidationError({
                    "fecha_creacion": [
                        f"Solo esta permitido una solicitud por día",
                        f"Actualice la solicitud con fecha de creación: {date.today()}"
                    ]
                })
        return super().create(validated_data)


class SolicitudReadSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    equipos = ClienteEquipoSerializer(many=True)
    jefe_equipo = JefeTrabajadorSerializer()

    class Meta:
        model = Solicitud
        fields = '__all__'
