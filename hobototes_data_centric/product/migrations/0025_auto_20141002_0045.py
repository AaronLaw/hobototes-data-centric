# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_topic_market_reference_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='campaign',
            field=models.ForeignKey(to='activity.Campaign', help_text='The campaign of this product topic'),
        ),
    ]
