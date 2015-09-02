# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20150505_1004'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actioninfo',
            unique_together=set([('action_name', 'object_name', 'object_info')]),
        ),
    ]
