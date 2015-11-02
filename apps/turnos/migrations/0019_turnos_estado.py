# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0018_auto_20151102_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='estado',
            field=models.CharField(default='ESPERA', max_length=25),
            preserve_default=False,
        ),
    ]
