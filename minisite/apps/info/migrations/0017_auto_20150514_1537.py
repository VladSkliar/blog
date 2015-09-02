# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20150505_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(related_name='contacts', to='info.Person'),
            preserve_default=True,
        ),
    ]
