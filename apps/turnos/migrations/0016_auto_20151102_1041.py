# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0015_sectores_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='sector',
            field=models.ForeignKey(to='turnos.Sectores'),
        ),
    ]
