# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='end_date',
            field=models.DateField(default='0001-01-01', help_text='Set to 0001-01-01 for non-ending campagin'),
        ),
    ]
