from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class signUpForm(ModelForm):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = models.User
#         fields = ('name', 'email', 'password')


# try login match
