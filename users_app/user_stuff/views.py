from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'forms': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('reservation')
            except:
                return render(request, 'signup.html', {
                'forms': UserCreationForm,
                'error' : "User already exists"
            })
              
        return render(request, 'signup.html', {
                'forms': UserCreationForm,
                'error' : "Passwords do not match"
        })

def reservation(request):
    return render(request, 'reservation.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'User name or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('reservation')

def signout(request):
    logout(request)
    return redirect('home')
