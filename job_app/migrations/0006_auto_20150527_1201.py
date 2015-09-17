# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_auto_20150527_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='company',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'Bachelor', b'Bachelor'), (b'Specialist', b'Specialist')]),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_position',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='location',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='references',
            field=models.ManyToManyField(to='job_app.Reference', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
