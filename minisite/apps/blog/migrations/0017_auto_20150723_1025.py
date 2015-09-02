# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20150722_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('post', models.PositiveSmallIntegerField()),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('ip_address', models.IPAddressField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.AlterUniqueTogether(
            name='postrating',
            unique_together=set([('user', 'post')]),
        ),
    ]
