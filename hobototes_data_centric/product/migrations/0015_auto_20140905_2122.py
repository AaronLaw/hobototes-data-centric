# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20140903_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='create_date',
            new_name='created',
        ),
    ]
