# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0033_auto_20150818_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(related_name='person', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='nickname',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
