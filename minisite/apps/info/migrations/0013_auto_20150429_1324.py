# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20150429_0903'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([('person', 'email')]),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
