# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0010_auto_20151102_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectores',
            name='codigo',
            field=models.CharField(default=b'A', max_length=2, null=True),
        ),
    ]
