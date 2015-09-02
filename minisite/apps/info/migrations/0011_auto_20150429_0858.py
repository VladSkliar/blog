# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20150429_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
            preserve_default=True,
        ),
    ]
