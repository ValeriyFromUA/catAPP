from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Confirmations
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
