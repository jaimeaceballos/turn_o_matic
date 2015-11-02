# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0013_auto_20151102_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectores',
            name='codigo',
        ),
    ]
