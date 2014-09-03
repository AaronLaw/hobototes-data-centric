# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20140901_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='types',
            new_name='catagory',
        ),
    ]
