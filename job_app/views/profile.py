from django.shortcuts import render
from django.http.response import HttpResponseRedirect

def profile(request):
    if request.user.is_authenticated():
        return render(request, 'profile/profile.html')
    else:
        return HttpResponseRedirect('/login/')
