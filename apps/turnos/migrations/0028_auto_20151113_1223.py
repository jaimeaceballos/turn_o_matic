# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0027_turnos_atencion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Turnos_atencion',
            new_name='TurnosAtencion',
        ),
    ]
