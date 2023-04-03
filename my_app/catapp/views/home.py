from django.views.generic import ListView
from ..models import Posts


class HomeView(ListView):
    template_name = 'home.html'
    model = Posts
    context_object_name = 'posts'
    extra_context = {'title': 'Home page'}
