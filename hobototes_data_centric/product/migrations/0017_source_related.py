# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20140905_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='related',
            field=models.ManyToManyField(null=True, to='product.Source', related_name='related_rel_+', blank=True),
            preserve_default=True,
        ),
    ]
