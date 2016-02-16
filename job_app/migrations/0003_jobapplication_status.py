# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0002_auto_20150507_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(default=datetime.datetime(2015, 5, 11, 17, 7, 56, 270580, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
