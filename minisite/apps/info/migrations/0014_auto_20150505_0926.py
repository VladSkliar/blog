# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20150429_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(related_name='contact', to='info.Person'),
            preserve_default=True,
        ),
    ]
