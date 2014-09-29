# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_remove_source_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='requirement',
            field=models.CharField(help_text='Does the source we find here RESTRICT TO what the topic product look like? (think about the outlook, the made of, etc...)', default='similar', max_length=50, choices=[('restrict', 'restrict to same'), ('similar', 'similar to is ok')]),
            preserve_default=True,
        ),
    ]
