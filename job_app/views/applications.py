from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from job_app.models import JobApplication
from job_app.forms import ApplicationForm


def applications(request):
    print request.POST
    if request.method == 'POST':
        if "add_record" in request.POST:
            return render(request, 'applications/new_record.html', {'form': ApplicationForm()})
        elif "save_record" in request.POST: # create new or change existing one
            return __save_record(request)
        elif 'apply' in request.POST:
            return HttpResponseRedirect('/')
    else:
        user = request.user
        if user.is_authenticated():
            apps = JobApplication.objects.filter(user=user)
            return render(request, 'applications/applications.html', {'app_list': apps})
        else:
            return HttpResponseRedirect('/login/')
    return render(request, 'applications/applications.html')

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

