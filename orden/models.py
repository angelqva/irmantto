from django.db import models
from trabajador.models import Trabajador
from helpers.helper import ESTADO_CHOICES_ORDEN
from solicitud.models import Solicitud
from tarea.models import Tarea
from cliente.models import Equipo


class Orden(models.Model):
    solicitud = models.ForeignKey(Solicitud, related_name="orden_trabajo", on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES_ORDEN, default='Pendiente')
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField(null=True, blank=True)
    trabajadores = models.ManyToManyField(Trabajador)
    tareas = models.ManyToManyField(Tarea, through="TareaOrden")

    def __str__(self):
        fecha_fin = "sin completar"
        if self.fecha_fin is not None:
            fecha_fin = str(self.fecha_fin)
        return f"Orden({str(self.solicitud)} inicio: {str(self.fecha_inicio)} fin: {fecha_fin})"


class TareaOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name="tarea_orden", on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, related_name="tarea_orden", on_delete=models.CASCADE)
    equipos = models.ForeignKey(Equipo, related_name="tarea_orden_equipos", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"TareaOrden ({str(self.orden)}, {str(self.tarea)}, cantidad_equipos: " \
               f"{str(self.equipos.objects.all().count())})"

