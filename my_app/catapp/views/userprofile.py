from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import User, Posts, Images
from django.views.generic import DetailView


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Posts.objects.filter(user_id=self.object.id)
        images = Images.objects.filter(post_id__user_id=self.object.id).select_related('post_id__user_id').first()
        context['posts'] = posts
        context['images'] = images
        return context
