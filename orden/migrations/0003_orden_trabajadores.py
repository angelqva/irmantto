# Generated by Django 3.1 on 2022-10-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajador', '0001_initial'),
        ('orden', '0002_auto_20221019_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='trabajadores',
            field=models.ManyToManyField(to='trabajador.Trabajador'),
        ),
    ]
