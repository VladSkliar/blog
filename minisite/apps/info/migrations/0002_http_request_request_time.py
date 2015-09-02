# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='http_request',
            name='request_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 18, 6, 30, 18951, tzinfo=utc), verbose_name=b'request_time'),
            preserve_default=False,
        ),
    ]
