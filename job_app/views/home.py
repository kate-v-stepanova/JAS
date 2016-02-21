from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.template import Template, Context
from django.core.mail import send_mail, EmailMessage

from job_app.models import CV, Reference, JobApplication

def __email(request):
    arguments = request.session['job_app_args']
    message = request.session['email']
    to = [request.POST.get('address')]

    context = Context(arguments)
    template = 'cover_letter_pdf.html'
    cover_letter = render_to_pdf(template, context)

    email = EmailMessage(subject=arguments.get('job_position'), body=message,
             bcc=['kate.v.stepanova@gmail.com'],
             from_email='kate.v.stepanova@gmail.com', to=to)
    email.content_subtype = "html"

    cv = CV.objects.first()
    if cv is None:
        return render(request, 'home.html', {'notification': 'No CV to attach. Please add a CV on the profile page'})

    email.attach('EkaterinaStepanova.CV.pdf', cv.file.read(), 'application/pdf')

    if 'vdom' in request.POST:
        vdom = Reference.objects.filter(name='vdom').first()
        if vdom is None:
            return render(request, 'home.html', {'notification': 'No VDOM reference to attach. '
                                                                 'Please add VDOM on the profile page'})

        email.attach('EkaterinaStepanova.Reference.VDOM.pdf', vdom.file.read(), 'application/pdf')
    if 'nec' in request.POST:
        nec = Reference.objects.filter(name='nec').first()
        if nec is None:
            return render(request, 'home.html', {'notification': 'No a reference reference to attach. '
                                                                 'Please add a reference on the profile page'})

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

