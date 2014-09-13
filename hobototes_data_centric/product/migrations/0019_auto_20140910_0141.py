# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20140909_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='key_idea',
            field=models.TextField(blank=True, help_text='How to find it. Use | to separate ideas'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='remark',
            field=models.TextField(verbose_name='Remark / Description /Features', blank=True, help_text='About the product itself.'),
        ),
    ]
