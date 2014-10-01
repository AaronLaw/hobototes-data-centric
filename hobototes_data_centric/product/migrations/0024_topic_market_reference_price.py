# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20141001_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='market_reference_price',
            field=models.DecimalField(decimal_places=2, help_text='In US Dollar', null=True, max_digits=6),
            preserve_default=True,
        ),
    ]
