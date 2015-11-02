# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0005_turnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramites',
            name='sector',
            field=models.ForeignKey(related_name='tramite_asociado', default=b'1', to='turnos.Sectores'),
        ),
    ]
