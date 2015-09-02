# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_http_request_request_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 3, 31, 15, 6, 47, 977240, tzinfo=utc), upload_to=None),
            preserve_default=False,
        ),
    ]
