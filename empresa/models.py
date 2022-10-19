from django.core.validators import RegexValidator
from django.db import models
from user.models import User
from cliente.models import Cliente


class Empresa(models.Model):
    registro = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(blank=False)
    telefono = models.CharField(blank=True, max_length=15, validators=[
        RegexValidator(
            r"^[0-9]*$", "Solo aceptan digitos")
    ])
    usuario = models.OneToOneField(User, related_name="empresa_usuario", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Empresa({self.registro} {self.nombre} {self.telefono})"


class Responsable(Cliente):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="responsables")

    def __str__(self):
        return f"Responsable({self.nombre}, {str(self.empresa)})"
