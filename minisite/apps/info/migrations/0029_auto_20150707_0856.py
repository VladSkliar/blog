# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0028_auto_20150703_0858'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actioninfo',
            unique_together=set([]),
        ),
    ]
