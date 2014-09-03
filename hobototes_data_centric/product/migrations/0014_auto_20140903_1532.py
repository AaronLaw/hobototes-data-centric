# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20140831_1934'),
        ('product', '0013_topic_purchase_adjectment'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='topic',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='purchase_adjectment',
            field=models.DecimalField(max_digits=6, default=0, decimal_places=2, help_text='to refine the final purchase'),
        ),
    ]
