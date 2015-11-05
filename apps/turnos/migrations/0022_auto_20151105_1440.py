# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0021_remove_boxatencion_turnoatencion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxatencion',
            name='clienteAtencion',
        ),
        migrations.RemoveField(
            model_name='boxatencion',
            name='tipoAtencion',
        ),
        migrations.RemoveField(
            model_name='boxatencion',
            name='tramiteAtencion',
        ),
        migrations.AddField(
            model_name='boxatencion',
            name='empleado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boxatencion',
            name='habilitado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='boxatencion',
            name='nro_box',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
