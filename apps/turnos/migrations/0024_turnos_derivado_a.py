# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0023_turnos_atendido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='derivado_a',
            field=models.ForeignKey(related_name='derivado', to='turnos.Sectores', null=True),
        ),
    ]
