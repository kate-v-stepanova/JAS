# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0003_jobapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cv',
            field=models.ForeignKey(blank=True, to='job_app.CV', null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='ml',
            field=models.ForeignKey(blank=True, to='job_app.MotivationLetter', null=True),
        ),
    ]
