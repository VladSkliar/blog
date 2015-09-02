# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0040_auto_20150820_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvite',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='userinvite',
            unique_together=set([('email', 'user')]),
        ),
    ]
