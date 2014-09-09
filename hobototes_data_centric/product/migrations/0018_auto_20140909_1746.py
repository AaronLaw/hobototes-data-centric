# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_source_related'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-count'], 'verbose_name_plural': 'Categories', 'verbose_name': 'Category'},
        ),
        migrations.AlterField(
            model_name='topic',
            name='remark',
            field=models.TextField(verbose_name='Remark / Description /Features', blank=True),
        ),
    ]
