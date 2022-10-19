# Generated by Django 3.1 on 2022-10-19 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orden', '0001_initial'),
        ('solicitud', '0001_initial'),
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orden_trabajo', to='solicitud.solicitud'),
        ),
        migrations.AddField(
            model_name='orden',
            name='tarea',
            field=models.ManyToManyField(to='tarea.Tarea'),
        ),
    ]
