# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20141007_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='resolution',
            field=models.CharField(default='D', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chart',
            name='symbol',
            field=models.CharField(default='AA', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chart',
            name='lastModified',
            field=models.DateTimeField(),
        ),
    ]
