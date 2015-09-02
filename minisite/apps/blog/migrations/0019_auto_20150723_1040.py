# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20150723_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrating',
            name='ip_address',
            field=models.IPAddressField(blank=True),
            preserve_default=True,
        ),
    ]
