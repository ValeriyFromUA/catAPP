from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse


class LoginView(View):

    @staticmethod
    def get(request):
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Username OR password does not exist')
            return render(request, 'login.html')

        login(request, user)
        return redirect(reverse('profile', args=[user.id]))
