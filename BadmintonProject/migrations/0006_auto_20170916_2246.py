# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('BadmintonProject', '0005_auto_20170817_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date_expense',
            field=models.DateField(default=datetime.date(2017, 9, 16)),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date_receipt',
            field=models.DateField(default=datetime.datetime(2017, 9, 16, 22, 46, 28, 720000)),
        ),
    ]
