# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0019_turnos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxatencion',
            name='sectores',
            field=models.ManyToManyField(to='turnos.Sectores'),
        ),
    ]
