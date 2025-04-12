from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm, SignInForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reservation')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    

def reservation(request):
    return render(request, 'reservation.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('reservation')
        else:
            return render(request, 'signin.html', {'form': form})
    else:
        form = SignInForm()
        return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')
