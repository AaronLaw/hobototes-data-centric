# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='tags',
            new_name='tag',
        ),
    ]
