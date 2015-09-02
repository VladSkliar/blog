# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0026_auto_20150616_1836'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actioninfo',
            unique_together=set([('action_name', 'object_name', 'object_info')]),
        ),
    ]
