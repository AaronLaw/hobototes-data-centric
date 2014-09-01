# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20140901_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='reason',
            field=models.CharField(max_length=255, default='It sells!', verbose_name='Why it is here?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seller',
            name='rating',
            field=models.IntegerField(default=3, help_text='1 to 5 stars'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='seller',
            field=models.ForeignKey(default=1, to='product.Seller', help_text='#1 reserves for virtual seller.'),
        ),
    ]
