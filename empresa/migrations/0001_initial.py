# Generated by Django 3.1 on 2022-10-19 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(blank=True, max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cliente.cliente')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsables', to='empresa.empresa')),
            ],
            bases=('cliente.cliente',),
        ),
    ]
