from __future__ import unicode_literals
from easy_pdf.rendering import render_to_pdf, render_to_pdf_response
import os
import datetime

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, models
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template import Template, Context
from django.template.loader import render_to_string

from models import CV, Reference, JobApplication
from forms import ApplicationForm


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'notification': 'Incorrect login or password'})
        else:
            auth_login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


# register
def register(request):
    if request.user.is_authenticated():
        auth_logout(request)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        user = models.User.objects.filter(username=username)
        if user:
            return render(request, 'auth/login.html', {'notification': 'User already exists'})
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        if password and password == confirm_password:
            user = models.User.objects.create_user(username, email, password)
            user.save()
            return login(request)
            # TODO: email confirm
            # return HttpResponseRedirect('/')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/') # TODO: redirect back


def __email(request):
    arguments = request.session['job_app_args']
    message = request.session['email']
    to = [request.POST.get('address')]

    context = Context(arguments)
    template = 'cover_letter_pdf.html'
    cover_letter = render_to_pdf(template, context)

    print request.POST

    email = EmailMessage(subject=arguments.get('job_position'), body=message,
             bcc=['kate.v.stepanova@gmail.com'],
             from_email='kate.v.stepanova@gmail.com', to=to)
    email.content_subtype = "html"



    cv = CV.objects.first()
    email.attach('EkaterinaStepanova.CV.pdf', cv.file.read(), 'application/pdf')

    if 'vdom' in request.POST:
        vdom = Reference.objects.filter(name='vdom').first()
        email.attach('EkaterinaStepanova.Reference.VDOM.pdf', vdom.file.read(), 'application/pdf')
    if 'nec' in request.POST:
        nec = Reference.objects.filter(name='nec').first()
        email.attach('EkaterinaStepanova.Reference.NEC.pdf', nec.file.read(), 'application/pdf')

    email.attach('EkaterinaStepanova.MotivationLetter.pdf', cover_letter, 'application/pdf')
    email.send()

    return render(request, 'home.html')


def cover_letter_pdf(request):
    if request.method == 'GET':
        return (request, 'cover_letter_pdf.html')
    else:

        arguments = {
            "hr_name": request.POST.get('hr_name'),
            "company": request.POST.get('company'),
            "company_url": request.POST.get('company_url'),
            "job_position": request.POST.get('job_position'),
            "job_areas": request.POST.get('job_areas'),
            "experience": request.POST.get('experience')
        }
        context = Context(arguments)
        template = 'cover_letter_pdf.html'
        return render_to_pdf_response(request, template, context)


def __cover_letter(request):
    arguments = {
        "hr_name": request.POST.get('hr_name'),
        "company": request.POST.get('company'),
        "company_url": request.POST.get('company_url'),
        "job_position": request.POST.get('job_position'),
        "job_areas": request.POST.get('job_areas'),
        "experience": request.POST.get('experience')
    }
    context = Context(arguments)

    email_body = render_to_string('email_body.html', context)
    template = Template(email_body)
    email = template.render(context)

    request.session['email'] = email
    request.session['job_app_args'] = arguments

    return render(request, 'email.html', arguments)


def home(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'cover_letter' in request.POST:
                return __cover_letter(request)

            elif 'email' in request.POST:
                return __email(request)
            else:
                return render(request, 'home.html')

        else:
            return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/login/')


def __save_record(request):
    # create a new one
    form = ApplicationForm(request.POST)
    if form.is_valid():
        user = request.user
        application = form.save(commit=False)
        application.user = user
        if not application.date:
            application.date = datetime.date.today()
        application.save()
        app_list = JobApplication.objects.filter(user=user)
        return render(request, 'applications/applications.html', {'app_list': app_list})
    else:
        return render(request, 'applications/new_record.html', {'form': form})



def applications(request):
    if request.method == 'POST':
        print request.POST
        if "add_record" in request.POST:
            return render(request, 'applications/new_record.html', {'form': ApplicationForm()})
        if "save_record" in request.POST: # create new or change existing one
            return __save_record(request)
    else:
        user = request.user
        if user.is_authenticated():
            apps = JobApplication.objects.filter(user=user)
            return render(request, 'applications/applications.html', {'app_list': apps})
        else:
            return HttpResponseRedirect('/login/')
    return render(request, 'applications/applications.html')


def send_application(request):
    print request
    if request.method == 'POST':
        print request.POST
    return render(request, "home.html")

