# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_actioninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioninfo',
            name='object_number',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
