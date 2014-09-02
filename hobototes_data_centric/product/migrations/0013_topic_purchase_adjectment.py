# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20140902_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='purchase_adjectment',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=0),
            preserve_default=True,
        ),
    ]
