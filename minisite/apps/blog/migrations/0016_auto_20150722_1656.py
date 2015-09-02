# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150722_1654'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('nickname', 'post_id')]),
        ),
    ]
