# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150624_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
