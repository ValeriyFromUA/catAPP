from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    is_confirmed = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Confirmations(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_key = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    name = models.CharField(max_length=100)


class Posts(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags, through='PostTags')


class Images(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    image_path = models.ImageField(blank=False)
    preview_image_path = models.ImageField()


class PostTags(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    is_liked = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
