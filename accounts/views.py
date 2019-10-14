from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect



def register(request):
    # Check if the request is POST method
    if request.method == 'POST':
        # The user needs to be registered
        if request.POST['password1'] == request.POST['password2']:
            try:
                # if password valid then check if the user already exists
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html', {'error': 'User is already registered'})
            except User.DoesNotExist:
                # if user does not exist then Register
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('portfolio:home')
        else:  # if passwords do not match throw an error
            return render(request, 'accounts/register.html', {'error': 'Passwords must match'})
    else:

        return render(request, 'accounts/register.html')