# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0026_turnos_fecha_fin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos_atencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.ForeignKey(to='turnos.Turnos')),
            ],
        ),
    ]
