from django.db import models
from django.core.validators import MinValueValidator


class Tarea(models.Model):
    codigo = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField(validators=[
        MinValueValidator(0)
    ])

    def __str__(self):
        return f"Tarea({self.codigo}-{self.precio})"
