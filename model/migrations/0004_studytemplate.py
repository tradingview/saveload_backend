# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20141008_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ownerSource', models.CharField(max_length=200)),
                ('ownerId', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('content', jsonfield.fields.JSONField()),
            ],
        ),
    ]
