# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0031_userinvite_is_send'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinvite',
            name='is_send',
        ),
    ]
