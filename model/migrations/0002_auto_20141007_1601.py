# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='lastModified',
            field=models.DateTimeField(default=datetime.date(2014, 10, 7), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='name',
            field=models.CharField(default='noname', max_length=200),
            preserve_default=False,
        ),
    ]
