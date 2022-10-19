from django.core.validators import RegexValidator
from django.db import models
from user.models import User


class Cliente(models.Model):
    carnet_identidad = models.CharField(unique=True, max_length=11, validators=[
        RegexValidator(
            r"^[0-9]*$", "Solo aceptan digitos")
    ])
    nombre = models.CharField(max_length=255, blank=True)
    apellidos = models.CharField(max_length=255, blank=True)
    direccion = models.TextField(blank=False)
    telefono = models.CharField(blank=True, max_length=15, validators=[
        RegexValidator(
            r"^[0-9]*$", "Solo aceptan digitos")
    ])
    usuario = models.OneToOneField(User, related_name="cliente_usuario", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Cliente({self.nombre} {self.apellidos} {self.telefono})"

