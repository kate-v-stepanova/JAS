# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import CV, Reference, JobApplication


class CVAdmin(admin.ModelAdmin):
    model = CV


class ReferenceAdmin(admin.ModelAdmin):
    model = Reference


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(CV, CVAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)

# from models import PersonalInformation, Experience, Education, Skills, LanguageSkills, Responsibility,
#
#
# class PersonalInformationAdmin(admin.ModelAdmin):
#     model = PersonalInformation
#
#
# class ExperienceAdmin(admin.ModelAdmin):
#     model = Experience
#
#
# class EducationAdmin(admin.ModelAdmin):
#     model = Education
#
#
# class SkillsAdmin(admin.ModelAdmin):
#     model = Skills
#
# class LanguageSkillsAdmin(admin.ModelAdmin):
#     model = LanguageSkills
#
#
# class RespAdmin(admin.ModelAdmin):
#     model = Responsibility
#
# admin.site.register(PersonalInformation, PersonalInformationAdmin)
# admin.site.register(Experience, ExperienceAdmin)
# admin.site.register(Education, EducationAdmin)
# admin.site.register(Skills, SkillsAdmin)
# admin.site.register(LanguageSkills, LanguageSkillsAdmin)
# admin.site.register(Responsibility, RespAdmin)
