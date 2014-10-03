# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20141002_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='weight',
            field=models.IntegerField(help_text='Estimate the weight of this product', default=0, max_length=4, blank=True),
            preserve_default=True,
        ),
    ]
