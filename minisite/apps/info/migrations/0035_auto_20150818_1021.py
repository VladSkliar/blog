# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0034_auto_20150818_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(related_name='person', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
