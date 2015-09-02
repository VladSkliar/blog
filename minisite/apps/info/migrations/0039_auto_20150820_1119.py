# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0038_userinvite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvite',
            name='code',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
