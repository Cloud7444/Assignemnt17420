from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1','password2']


class ListAuthor(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','comment','caption','pic']