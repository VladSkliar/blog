# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20150403_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Time of action')),
                ('action_name', models.CharField(max_length=50)),
                ('object_name', models.CharField(max_length=50)),
                ('object_number', models.PositiveSmallIntegerField(verbose_name=b'Object id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
