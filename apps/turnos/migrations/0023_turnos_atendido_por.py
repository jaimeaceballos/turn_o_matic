# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0022_auto_20151105_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='atendido_por',
            field=models.ForeignKey(to='turnos.BoxAtencion', null=True),
        ),
    ]
