# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from settings import DEGREE_OPTIONS, STATIC_ROOT


class Reference(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to=STATIC_ROOT)


class MotivationLetter(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to=STATIC_ROOT)

    def __str__(self):
        return self.name


class CV(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to=STATIC_ROOT)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    user = models.ForeignKey(User, default=None)
    company = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    job_position = models.CharField(max_length=50, null=True, blank=True)
    job_url = models.URLField(null=True, blank=True)
    date = models.DateField(null=True, blank=True, verbose_name="Application date")#, input_formats=DATE_INPUT_FORMATS)
    ml = models.ForeignKey(MotivationLetter, blank=True, null=True, verbose_name="Motivation Letter")
    cv = models.ForeignKey(CV, blank=True, null=True, verbose_name="CV")
    references = models.ManyToManyField(Reference, blank=True)
    degree = models.CharField(choices=DEGREE_OPTIONS, max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.location + ' ' + self.job_position


class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    objective = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Responsibility(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Experience(models.Model):
    dates = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    responsibilities = models.ManyToManyField(Responsibility)

    def __str__(self):
        return self.company + ', ' + self.position


class Education(models.Model):
    dates = models.CharField(max_length=30)
    degree = models.CharField(max_length=50)
    area_of_studies = models.CharField(max_length=50)
    educational_institue = models.CharField(max_length=100)

    def __str__(self):
        return self.degree + ', ' + self.area_of_studies


class LanguageSkills(models.Model):
    language = models.CharField(max_length=20)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.language + ': ' + self.level


class Skills(models.Model):
    languages = models.ManyToManyField(LanguageSkills)
    programming_languages = models.CharField(max_length=100)
    operating_systems = models.CharField(max_length=100)
    databases = models.CharField(max_length=100)
    web_technologies = models.CharField(max_length=100)
    other_technologies = models.CharField(max_length=100)
    personal_skills = models.CharField(max_length=100)