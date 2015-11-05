# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0020_boxatencion_sectores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxatencion',
            name='turnoAtencion',
        ),
    ]
