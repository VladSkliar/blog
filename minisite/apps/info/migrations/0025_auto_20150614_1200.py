# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0024_auto_20150610_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(max_length=50, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
