# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20150421_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='actioninfo',
            name='object_info',
            field=models.CharField(default=datetime.datetime(2015, 4, 21, 15, 43, 56, 366096, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
