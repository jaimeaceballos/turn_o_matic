# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0025_turnos_tramite'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='fecha_fin',
            field=models.DateTimeField(null=True),
        ),
    ]
