# Generated by Django 3.1 on 2022-10-18 03:07

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
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255)),
                ('apellidos', models.CharField(blank=True, max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='cliente.cliente')),
            ],
        ),
    ]