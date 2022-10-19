from django.db import models
from trabajador.models import Trabajador
from helpers.helper import ESTADO_CHOICES_ORDEN
from solicitud.models import Solicitud
from tarea.models import Tarea


class Orden(models.Model):
    solicitud = models.ForeignKey(Solicitud, related_name="orden_trabajo", on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES_ORDEN, default='Pendiente')
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField(null=True, blank=True)
    trabajadores = models.ManyToManyField(Trabajador)
    tarea = models.ManyToManyField(Tarea)

    def __str__(self):
        fecha_fin = "sin completar"
        if self.fecha_fin is not None:
            fecha_fin = str(self.fecha_fin)
        return f"Orden({str(self.solicitud)} inicio: {str(self.fecha_inicio)} fin: {fecha_fin})"
