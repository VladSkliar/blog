# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0030_userinvite'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvite',
            name='is_send',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
