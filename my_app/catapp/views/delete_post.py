from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from ..models import Posts


class DeletePostView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, pk):
        post = get_object_or_404(Posts, id=pk)
        if request.user.id == post.user_id.id:
            post.delete()
        return redirect(reverse("profile", args=[request.user.id]))
