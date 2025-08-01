from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return render(request, 'authentication/dashboard.html', {})
        else:
            messages.error(request, 'Invalid username or password.')
            return HttpResponse(
                render(request, 'authentication/login.html', {}),
                status=401
            )
    else:
        return render(request, 'authentication/login.html', {})