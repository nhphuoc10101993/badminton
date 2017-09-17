# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BadmintonProject', '0004_auto_20170806_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id_expense', models.AutoField(serialize=False, primary_key=True)),
                ('date_expense', models.DateField(default=datetime.date(2017, 8, 17))),
                ('money', models.IntegerField(default=0)),
                ('reason', models.TextField()),
                ('expense_person', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date_receipt',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 22, 41, 43, 882000)),
        ),
    ]
