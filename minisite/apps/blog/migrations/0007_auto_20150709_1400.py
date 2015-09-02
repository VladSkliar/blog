# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150709_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 14, 0, 0, 429359, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
