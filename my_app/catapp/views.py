from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.contrib import messages

from catogramm.settings import BASE_DIR
from .forms import NewUserForm
from .models import User, Confirmations, Posts, Likes, Tags, Images, PostTags


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, 'Username OR password does not exit')
        return redirect('home')

    context = {'page': page}
    return render(request, 'catapp/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'register.html', {'form': form})


def home(request):
    context = 'users'
    return render(request, 'base/home.html', context)
