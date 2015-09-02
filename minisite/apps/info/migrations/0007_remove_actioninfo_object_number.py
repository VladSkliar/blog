# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20150421_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioninfo',
            name='object_number',
        ),
    ]
