# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0017_auto_20151102_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='no_cliente',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
    ]
