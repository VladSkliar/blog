# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0023_person_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioninfo',
            name='date',
            field=models.DateField(verbose_name=b'Action date'),
            preserve_default=True,
        ),
    ]
