# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_auto_20150527_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'photos/', blank=True),
            preserve_default=True,
        ),
    ]
