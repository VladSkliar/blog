# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20150429_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='jabber',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='other_contacts',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='skype_id',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
