# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0006_tramites_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnos',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
