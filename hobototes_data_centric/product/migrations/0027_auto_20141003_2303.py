# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_topic_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='weight',
            field=models.IntegerField(help_text='Estimate the weight of this product', blank=True, max_length=4),
        ),
    ]
