# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='post',
            new_name='post_id',
        ),
    ]
