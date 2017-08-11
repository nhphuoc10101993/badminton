# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('BadmintonProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date_receipt',
            field=models.DateField(default=datetime.datetime(2017, 8, 1, 21, 45, 38, 341000)),
        ),
    ]
