from random import randrange

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from catogramm.settings import BASE_DIR
from cofirmation import send_confirmation_email
from .forms import NewUserForm, UserForm, ConfirmationForm
from .models import User, Confirmations, Posts, Likes, Tags, Images, PostTags


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Username OR password does not exit')
        login(request, user)
        return redirect(reverse('profile', args=[user.id]))

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            key = randrange(10000, 99999)
            confirmation = Confirmations(user_id=user, confirmation_key=key)
            confirmation.save()
            send_confirmation_email(user.email, key)
            return redirect('confirm')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'register.html', {'form': form})


def confirm(request):
    if request.method == 'POST':
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            confirmation_key = form.cleaned_data['confirmation_key']
            confirmation = Confirmations.objects.filter(confirmation_key=confirmation_key).first()
            if confirmation is not None:
                user = confirmation.user_id
                user.is_confirmed = True
                user.save()
                confirmation.delete()
                return redirect(reverse('edit_profile', args=[user.id]))
            else:
                form.add_error('confirmation_key', 'invalid code')
    else:
        form = ConfirmationForm()
    return render(request, 'confirmation.html', {'form': form})


@login_required
def edit_profile(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.bio = form.cleaned_data['bio']
            if form.cleaned_data['avatar']:
                user.avatar = form.cleaned_data['avatar']
            user.save()
            return redirect(reverse('profile', args=[pk]))
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)
