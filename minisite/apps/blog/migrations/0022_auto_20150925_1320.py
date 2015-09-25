# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_post_last_modified'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postrating',
            unique_together=set([]),
        ),
    ]
