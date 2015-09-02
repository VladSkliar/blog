# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_auto_20150505_0926'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='contact',
            order_with_respect_to='person',
        ),
    ]
