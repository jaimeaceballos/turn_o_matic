# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0014_remove_sectores_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectores',
            name='codigo',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
