from django.core.validators import RegexValidator, MinLengthValidator
from user.models import *


class Cargo(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cargo-{self.nombre}"


class Trabajador(models.Model):
    carnet_identidad = models.CharField(unique=True, max_length=11, validators=[
        MinLengthValidator(5, "No debe tener menos de 5 caracteres"),
        RegexValidator(r"^[0-9]*$", "Solo aceptan digitos")
    ])
    nombre = models.CharField(max_length=255, blank=True)
    apellidos = models.CharField(max_length=255, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(blank=True, max_length=15)
    escolaridad = models.CharField(blank=True, max_length=50)
    categoria = models.CharField(blank=True, max_length=50)
    cargo = models.ForeignKey(Cargo, related_name="trabajadores", on_delete=models.CASCADE, null=True, blank=True)
    jefe_equipo = models.ForeignKey("trabajador.Trabajador", on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name='trabajadores_jefe_equipo')
    usuario = models.OneToOneField(User, related_name="trabajador_usuario",
                                   on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Trabajador({self.nombre} {self.apellidos})"
