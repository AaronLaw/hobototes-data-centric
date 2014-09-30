# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default='0001-01-01')),
                ('remark', models.TextField(help_text='About the sourcing campaign.', verbose_name='Remark / Description', blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-start_date'],
                'managed': True,
                'verbose_name_plural': 'Campaigns',
                'verbose_name': 'Campaign',
            },
            bases=(models.Model,),
        ),
    ]
