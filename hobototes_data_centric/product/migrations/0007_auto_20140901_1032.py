# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20140901_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='reason',
            field=models.CharField(verbose_name='Why it is here?', max_length=255),
        ),
    ]
