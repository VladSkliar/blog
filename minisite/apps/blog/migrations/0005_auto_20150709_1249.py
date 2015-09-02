# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150709_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 12, 49, 10, 590759, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
