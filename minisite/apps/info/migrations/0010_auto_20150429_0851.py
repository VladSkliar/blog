# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_actioninfo_object_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=100)),
                ('jabber', models.CharField(max_length=50)),
                ('skype_id', models.CharField(max_length=50)),
                ('other_contacts', models.CharField(max_length=100)),
                ('person', models.ForeignKey(to='info.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Http_request',
            new_name='HTTPRequest',
        ),
        migrations.RemoveField(
            model_name='personcontact',
            name='person',
        ),
        migrations.DeleteModel(
            name='PersonContact',
        ),
        migrations.RenameField(
            model_name='httprequest',
            old_name='request_text',
            new_name='path',
        ),
        migrations.RenameField(
            model_name='httprequest',
            old_name='request_time',
            new_name='time',
        ),
    ]
