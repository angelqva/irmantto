# Generated by Django 3.1 on 2022-10-20 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Terminado', 'Terminado')], default='Pendiente', max_length=20)),
                ('fecha_inicio', models.DateField(auto_now=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TareaOrden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarea_orden_equipos', to='cliente.equipo')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_orden', to='orden.orden')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_orden', to='tarea.tarea')),
            ],
        ),
    ]
