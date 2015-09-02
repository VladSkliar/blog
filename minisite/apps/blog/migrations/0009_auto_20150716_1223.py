# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150716_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
