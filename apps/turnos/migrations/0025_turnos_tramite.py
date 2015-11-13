# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0024_turnos_derivado_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='tramite',
            field=models.ForeignKey(to='turnos.Tramites', null=True),
        ),
    ]
