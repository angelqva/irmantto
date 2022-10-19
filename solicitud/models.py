from django.db import models
from cliente.models import Cliente, Equipo
from trabajador.models import Trabajador
from helpers.helper import ESTADO_CHOICES_SOLICITUD


class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente, related_name="solicitudes", on_delete=models.CASCADE)
    equipos = models.ManyToManyField(Equipo)
    jefe_equipo = models.ForeignKey(Trabajador, on_delete=models.SET_NULL, null=True,
                                    related_name='solicitudes_jefe_equipo')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES_SOLICITUD, default='Pendiente')
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f"Solicitud({str(self.cliente)} {self.estado} {str(self.fecha)} {str(self.jefe_equipo)})"
