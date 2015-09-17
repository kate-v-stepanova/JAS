# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('job_position', models.CharField(max_length=50)),
                ('job_url', models.URLField()),
                ('date', models.DateField()),
                ('degree', models.CharField(max_length=50, choices=[(b'Bachelor', b'Bachelor'), (b'Specialist', b'Specialist')])),
                ('location', models.CharField(max_length=50)),
                ('cv', models.ForeignKey(to='job_app.CV', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MotivationLetter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='ml',
            field=models.ForeignKey(to='job_app.MotivationLetter', blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='references',
            field=models.ManyToManyField(to='job_app.Reference'),
        ),
    ]
