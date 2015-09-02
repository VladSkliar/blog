# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0037_auto_20150819_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='code',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
