# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150709_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=128),
            preserve_default=True,
        ),
    ]
