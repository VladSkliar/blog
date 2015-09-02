# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_remove_actioninfo_object_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioninfo',
            name='date',
            field=models.DateTimeField(verbose_name=b'Action time'),
            preserve_default=True,
        ),
    ]
