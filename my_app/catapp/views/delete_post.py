from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from ..models import Posts


class DeletePostView(LoginRequiredMixin, View):
    template_name = 'post.html'

    def get(self, request, pk):
        post = get_object_or_404(Posts, id=pk)
        return render(request, self.template_name, {'post': post})

    @staticmethod
    def post(request, pk):
        post = get_object_or_404(Posts, id=pk)
        print(post)
        if request.user.id == post.user_id.id:
            post.delete()
            return redirect(reverse('profile', args=[request.user.id]))
