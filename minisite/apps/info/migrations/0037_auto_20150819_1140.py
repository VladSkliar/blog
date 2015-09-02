# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0036_auto_20150819_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='user',
            field=models.ForeignKey(related_name='info', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
    ]
