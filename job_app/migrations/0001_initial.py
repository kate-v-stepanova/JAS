# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dates', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=50)),
                ('area_of_studies', models.CharField(max_length=50)),
                ('educational_institue', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dates', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('objective', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programming_languages', models.CharField(max_length=100)),
                ('operating_systems', models.CharField(max_length=100)),
                ('databases', models.CharField(max_length=100)),
                ('web_technologies', models.CharField(max_length=100)),
                ('other_technologies', models.CharField(max_length=100)),
                ('personal_skills', models.CharField(max_length=100)),
                ('languages', models.ManyToManyField(to='job_app.LanguageSkills')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities',
            field=models.ManyToManyField(to='job_app.Responsibility'),
        ),
    ]
