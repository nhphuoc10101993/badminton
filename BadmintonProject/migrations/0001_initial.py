# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id_receipt', models.AutoField(primary_key=True, serialize=False)),
                ('cashier', models.CharField(max_length=30)),
                ('date_receipt', models.DateField(default=datetime.datetime(2017, 8, 1, 9, 54, 32, 738647))),
                ('money', models.IntegerField(default=0)),
                ('reason', models.TextField()),
                ('receipt_person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
