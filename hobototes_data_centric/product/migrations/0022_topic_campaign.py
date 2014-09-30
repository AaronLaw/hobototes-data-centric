# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
        ('product', '0021_topic_requirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='campaign',
            field=models.ForeignKey(default=1, to='activity.Campaign'),
            preserve_default=True,
        ),
    ]
