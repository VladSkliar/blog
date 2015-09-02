# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20150723_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrating',
            name='user',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
