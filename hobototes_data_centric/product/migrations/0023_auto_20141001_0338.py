# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_topic_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='campaign',
            field=models.ForeignKey(help_text='The campaign of this product topic', to='activity.Campaign', default=1),
        ),
    ]
