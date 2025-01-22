from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import User
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm

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


@login_required
def update(request):
    if request.method == "POST":
        # Инициализируем форму с данными из POST-запроса
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            # Сохраняем изменения пользователя (только first_name и last_name)
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))  # Перенаправление на страницу профиля
    else:
        # Если GET-запрос, отображаем форму с текущими данными пользователя
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'update.html', context)

@login_required
def delete(request):
    user = request.user
    user.delete()
    return HttpResponseRedirect(reverse('user:index'))