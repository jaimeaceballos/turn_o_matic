# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sector', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(to='turnos.Cliente')),
            ],
        ),
    ]
