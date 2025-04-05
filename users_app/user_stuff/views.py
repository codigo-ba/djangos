from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reservation')
        else:
            return render(request, 'signup.html', {'forms': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'forms': form})
    

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
