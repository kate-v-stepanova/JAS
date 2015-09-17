# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_app', '0006_auto_20150527_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='references',
            field=models.ManyToManyField(to='job_app.Reference', blank=True),
        ),
    ]
