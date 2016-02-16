from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.forms.models import model_to_dict, fields_for_model
from django import forms

from models import JobApplication
from settings import DATE_FORMAT


class ApplicationForm(ModelForm):
    date = forms.DateField(required=False, input_formats=[DATE_FORMAT])
    class Meta:
        model = JobApplication
        exclude = ['references', 'user']
