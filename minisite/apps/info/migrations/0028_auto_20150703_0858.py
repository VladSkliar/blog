# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0027_auto_20150703_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(related_name='contacts', to='info.Person', unique=True),
            preserve_default=True,
        ),
    ]
