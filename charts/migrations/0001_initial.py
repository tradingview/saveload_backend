# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ownerSource', models.CharField(max_length=200)),
                ('ownerId', models.CharField(max_length=200)),
                ('content', jsonfield.fields.JSONField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
