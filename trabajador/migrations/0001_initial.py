# Generated by Django 3.1 on 2022-10-19 12:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet_identidad', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(5, 'No debe tener menos de 5 caracteres'), django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('escolaridad', models.CharField(blank=True, max_length=50)),
                ('categoria', models.CharField(blank=True, max_length=50)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='trabajador.cargo')),
                ('jefe_equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trabajadores_jefe_equipo', to='trabajador.trabajador')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trabajador_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]