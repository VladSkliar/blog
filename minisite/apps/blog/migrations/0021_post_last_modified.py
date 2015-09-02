# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20150723_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor=b'text', blank=True),
            preserve_default=True,
        ),
    ]
