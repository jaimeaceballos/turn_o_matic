# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxAtencion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turnoAtencion', models.CharField(max_length=999)),
                ('clienteAtencion', models.ForeignKey(to='turnos.Cliente')),
                ('tipoAtencion', models.ForeignKey(to='turnos.TipoCliente')),
                ('tramiteAtencion', models.ForeignKey(to='turnos.Tramites')),
            ],
        ),
    ]
