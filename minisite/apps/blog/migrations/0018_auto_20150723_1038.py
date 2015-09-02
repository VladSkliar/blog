# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20150723_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrating',
            name='ip_address',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
    ]
