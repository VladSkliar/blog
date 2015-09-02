# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0029_auto_20150707_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('user', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
