# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0032_remove_userinvite_is_send'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HTTPRequest',
            new_name='UserRequest',
        ),
    ]
