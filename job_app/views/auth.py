from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, models

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

