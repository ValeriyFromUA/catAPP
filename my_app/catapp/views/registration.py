from random import randrange
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from cofirmation import send_confirmation_email
from ..forms import NewUserForm
from ..models import Confirmations


class RegistrationView(View):
    extra_context = {'title': 'Registration'}

    @staticmethod
    def get(request):
        form = NewUserForm()
        return render(request, 'register.html', {'form': form})

    @staticmethod
    def post(request):
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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        key = randrange(10000, 99999)
        confirmation = Confirmations(user_id=user, confirmation_key=key)
        confirmation.save()
        send_confirmation_email(user.email, key)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'An error occurred during registration')
        return super().form_invalid(form)
