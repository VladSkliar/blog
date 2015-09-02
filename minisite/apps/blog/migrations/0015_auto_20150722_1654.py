# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20150722_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='post_id',
            field=models.PositiveSmallIntegerField(),
            preserve_default=True,
        ),
    ]
