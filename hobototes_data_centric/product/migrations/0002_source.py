# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('types', models.CharField(max_length=16, blank=True, null=True)),
                ('link', models.URLField()),
                ('status', models.CharField(max_length=20)),
                ('shop', models.CharField(blank=True, help_text='25 means this product is a virtual product.', max_length=50)),
                ('title', models.CharField(blank=True, max_length=1000)),
                ('material', models.CharField(blank=True, help_text='Use COMMA in ENGLISH to separate, not a Chinese comma', max_length=50)),
                ('purchase', models.DecimalField(max_digits=6, default=0, decimal_places=2)),
                ('min_quantity', models.PositiveIntegerField(blank=True, default=1, help_text='The starting quantity of purchase')),
                ('min_purchase', models.DecimalField(max_digits=6, blank=True, help_text='The possible lowest purchase.', null=True, decimal_places=2)),
                ('quantity_of_min_purchase', models.PositiveIntegerField(blank=True)),
                ('remark', models.CharField(blank=True, max_length=255)),
                ('acceptability', models.CharField(blank=True, help_text='A reference from buyers\' comments (aka. The product quality). Help to make decision on buy it or not. "Good" does not mean to buy', max_length=4)),
                ('ref', models.TextField(blank=True, verbose_name='The way it was found')),
                ('topic', models.ForeignKey(default=25, to='product.Topic')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
