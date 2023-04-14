from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Posts, User


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Posts.objects.filter(user_id=self.object.id).order_by("-created_at")
        context["posts"] = posts
        return context
