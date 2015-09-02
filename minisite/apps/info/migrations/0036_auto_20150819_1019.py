# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0035_auto_20150818_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthdate', models.DateField(verbose_name=b'Date of birth')),
                ('bio', models.CharField(max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'photos/', blank=True)),
                ('jabber', models.CharField(max_length=50, null=True, blank=True)),
                ('skype', models.CharField(max_length=50, null=True, blank=True)),
                ('other_contacts', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.ForeignKey(related_name='person', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=None,
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterUniqueTogether(
            name='info',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]
