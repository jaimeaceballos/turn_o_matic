# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_sector', models.CharField(max_length=50)),
                ('descripcion_sector', models.CharField(max_length=200)),
            ],
        ),
    ]
