from rest_framework import serializers
from rest_framework.validators import ValidationError
from solicitud.models import Solicitud
from trabajador.models import Trabajador
from cliente.models import Equipo
from .models import Orden, TareaOrden
from datetime import date
from solicitud.serializers import SolicitudReadSerializer
from trabajador.serializers import TrabajadorReadSerializer
from tarea.serializers import TareaSerializer, Tarea


class OrdenSerializer(serializers.ModelSerializer):
    solicitud = serializers.PrimaryKeyRelatedField(queryset=Solicitud.objects.all())
    trabajadores = serializers.PrimaryKeyRelatedField(many=True, queryset=Trabajador.objects.all())
    fecha_inicio = serializers.DateField(default=date.today())

    class Meta:
        model = Orden
        fields = ('id', 'solicitud', 'trabajadores', 'fecha_inicio', 'fecha_fin', 'estado')
        extra_kwargs = {
            "id": {"read_only": True},
        }


class OrdenReadSerializer(serializers.ModelSerializer):
    solicitud = SolicitudReadSerializer()
    trabajadores = TrabajadorReadSerializer(many=True)
    tareas = TareaSerializer(many=True)

    class Meta:
        model = Orden
        fields = '__all__'


class TareaOrdenSerializer(serializers.ModelSerializer):
    orden = serializers.PrimaryKeyRelatedField(queryset=Orden.objects.all())
    tarea = serializers.PrimaryKeyRelatedField(queryset=Tarea.objects.all())
    equipos = serializers.PrimaryKeyRelatedField(many=True, queryset=Equipo.objects.all())

    class Meta:
        model = TareaOrden
        fields = '__all__'


