# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150709_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2015, 7, 9, 12, 49, 47, 967817, tzinfo=utc), null=True, blank=True),
            preserve_default=True,
        ),
    ]
