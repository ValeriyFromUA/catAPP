from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=30)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'is_confirmed': self.is_confirmed,
            'created_at': self.created_at,
        }


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

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'likes_count': self.likes_count,
            'dislikes_count': self.dislikes_count,
            'images': [img.to_dict() for img in self.all_images.all()],
            'tags': [tag.name for tag in self.tags.all()]
        }


class Images(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='all_images')
    image_path = models.ImageField(blank=False)
    preview_image_path = models.ImageField()

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'image_path': self.image_path,
            'preview_image_path': self.preview_image_path,
        }


class PostTags(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Likes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    is_liked = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
