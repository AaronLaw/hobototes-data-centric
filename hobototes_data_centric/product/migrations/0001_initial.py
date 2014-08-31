# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('size', models.CharField(choices=[('light', 'Light'), ('medium', 'Medium'), ('heavy', 'Heavy')], blank=True, default='medium', max_length=10)),
                ('seller', models.IntegerField(help_text='#1 reserves for virtual seller.', default=1)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True, max_length=250)),
                ('status', models.CharField(choices=[('new', 'new'), ('in progress', 'in progress'), ('resloved', 'resloved'), ('closed', 'closed'), ('rejected', 'rejected')], default='new', max_length=16)),
                ('tag', models.CharField(help_text='Use COMMA in ENGLISH to separate, not a Chinese comma', blank=True, max_length=50)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2, null=True)),
                ('key_idea', models.TextField(help_text='Use | to separate ideas', blank=True)),
                ('remark', models.CharField(blank=True, verbose_name='Remark / Description /Features', max_length=255)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Product Topics',
                'verbose_name': 'Product Topic',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
