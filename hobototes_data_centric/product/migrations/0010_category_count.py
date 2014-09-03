# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20140902_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
