from django.db import models
from cliente.models import Cliente
from solicitud.models import Solicitud


class Equipo(models.Model):
    cliente = models.ForeignKey(Cliente, related_name="equipos", on_delete=models.CASCADE)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    marca = models.CharField(blank=False, null=False, max_length=50)
    ubicacion = models.CharField(blank=False, null=False, max_length=100)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Equipo({self.nombre}, {str(self.cliente)})"
