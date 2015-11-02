# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0007_auto_20151102_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectores',
            name='codigo',
            field=models.CharField(default=None, max_length=2),
            preserve_default=False,
        ),
    ]
