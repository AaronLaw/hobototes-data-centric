# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2014, 9, 1), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='series',
            field=models.CharField(default='Fashionable', max_length=16, choices=[('Fashionable', 'Fashionable'), ('Home & Garden', 'Home & Garden'), ('Not-another series', 'Not-another series')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='source',
            name='acceptability',
            field=models.CharField(blank=True, max_length=4, help_text='A reference from buyers\' comments (aka. The product quality). Help to make decision on buy it or not. "Good" does not mean to buy', choices=[('bad', 'bad'), ('ok', 'seems ok'), ('good', 'Good!')]),
        ),
        migrations.AlterField(
            model_name='source',
            name='quantity_of_min_purchase',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='status',
            field=models.CharField(default='inbox', max_length=20, help_text='The workflow. Make decision to buy it or not', choices=[('inbox', 'inbox'), ('reject', 'reject'), ('approved', 'approved'), ('bought', 'bought'), ('watch list', 'watch list'), ('expired', 'expried')]),
        ),
    ]
