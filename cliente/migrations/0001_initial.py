# Generated by Django 3.1 on 2022-10-20 04:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet_identidad', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
                ('nombre', models.CharField(blank=True, max_length=255)),
                ('apellidos', models.CharField(blank=True, max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
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
