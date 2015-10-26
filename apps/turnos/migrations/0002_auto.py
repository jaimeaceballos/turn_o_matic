# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patente', models.CharField(max_length=12)),
                ('marca_modelo', models.CharField(max_length=100)),
            ],
        ),
    ]
