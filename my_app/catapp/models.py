from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg", upload_to='users/avatar/')
    is_confirmed = models.BooleanField(default=False)


class Confirmations(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Posts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    preview_image = models.ImageField(blank=True, upload_to=f'posts/preview/')


class Images(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, upload_to=f'posts/images/')


class PostTags(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, blank=True)


class Likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    is_liked = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
