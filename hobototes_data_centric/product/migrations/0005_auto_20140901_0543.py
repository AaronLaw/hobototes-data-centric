# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20140901_0426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('shop', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField(default=3, verbose_name='1 to 5 stars')),
                ('remark', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name_plural': 'Sources', 'ordering': ['-modified'], 'verbose_name': 'Source'},
        ),
        migrations.AlterField(
            model_name='topic',
            name='price',
            field=models.DecimalField(help_text='In US Dollar', max_digits=6, null=True, decimal_places=2),
        ),
    ]
