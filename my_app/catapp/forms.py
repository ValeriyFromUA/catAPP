from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Images, Posts, PostTags
from django import forms


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'avatar']


class ConfirmationForm(forms.Form):
    confirmation_key = forms.CharField(label='confirmation key', max_length=50)


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description']


class TagsForm(ModelForm):
    class Meta:
        model = PostTags
        fields = ['tag']


class ImagesForm(ModelForm):
    image_path = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Images
        fields = ['image']
