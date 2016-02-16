# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0004_auto_20150527_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cv',
            field=models.ForeignKey(verbose_name='CV', blank=True, to='job_app.CV', null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='ml',
            field=models.ForeignKey(verbose_name='Motivation Letter', blank=True, to='job_app.MotivationLetter', null=True),
        ),
    ]
