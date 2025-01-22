from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import User
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:index'))

