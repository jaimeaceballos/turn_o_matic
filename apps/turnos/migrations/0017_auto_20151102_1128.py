# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0016_auto_20151102_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='no_cliente',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turnos',
            name='cliente',
            field=models.ForeignKey(to='turnos.Cliente', null=True),
        ),
    ]
