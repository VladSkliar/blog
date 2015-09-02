# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to=b'photos'),
            preserve_default=True,
        ),
    ]
