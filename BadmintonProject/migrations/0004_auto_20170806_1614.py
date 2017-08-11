# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('BadmintonProject', '0003_auto_20170806_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date_receipt',
            field=models.DateField(default=datetime.datetime(2017, 8, 6, 16, 14, 1, 3000)),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='receipt_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
