from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from ..forms import UserForm
from ..models import User


class EditProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request, pk):
        user = get_object_or_404(User, id=pk)
        form = UserForm(instance=user)
        return render(request, "edit_profile.html", {"form": form})

    @staticmethod
    def post(request, pk):
        user = get_object_or_404(User, id=pk)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.bio = form.cleaned_data["bio"]
            if form.cleaned_data["avatar"]:
                user.avatar = form.cleaned_data["avatar"]
            user.save()
            return redirect(reverse("profile", args=[pk]))
        return render(request, "edit_profile.html", {"form": form})
