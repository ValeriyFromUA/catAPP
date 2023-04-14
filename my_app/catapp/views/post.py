from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from ..models import Images, Likes, Posts, PostTags


class PostView(LoginRequiredMixin, View):
    template_name = "post.html"

    def get(self, request, pk):
        post = get_object_or_404(Posts, id=pk)
        images = Images.objects.filter(post_id=pk).all()
        tags = PostTags.objects.filter(post_id=pk).all()

        likes_count = Likes.objects.filter(post_id=post, is_liked=True).count()
        dislikes_count = Likes.objects.filter(post_id=post, is_liked=False).count()

        context = {
            "post": post,
            "images": images,
            "tags": tags,
            "likes_count": likes_count,
            "dislikes_count": dislikes_count,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(Posts, id=pk)
        user = request.user
        is_liked = bool(request.POST.get("is_liked"))

        like = Likes.objects.filter(user_id=user, post_id=post).first()
        if like:

            if like.is_liked == is_liked:
                like.delete()
            else:
                like.is_liked = is_liked
                like.save()
        else:
            Likes.objects.create(user_id=user, post_id=post, is_liked=is_liked)
        return redirect("post", pk=pk)
