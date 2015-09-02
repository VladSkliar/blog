# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0039_auto_20150820_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='is_accept',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='code',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
