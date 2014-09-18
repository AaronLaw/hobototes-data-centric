# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20140910_0141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='related',
        ),
    ]
