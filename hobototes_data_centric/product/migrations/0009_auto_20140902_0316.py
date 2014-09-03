# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20140902_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
                'managed': True,
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='source',
            name='catagory',
        ),
        migrations.AddField(
            model_name='source',
            name='category',
            field=models.ForeignKey(default=1, to='product.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='source',
            name='series',
            field=models.CharField(max_length=20, choices=[('Fashionable', 'Fashionable'), ('Home & Garden', 'Home & Garden'), ('Not-another series', 'Not-another series')]),
        ),
    ]
