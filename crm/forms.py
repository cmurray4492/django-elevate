from django.forms import ModelForm
from . models import Task
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class TaskForm(ModelForm):
    """Metadata"""
    class Meta:
        model = Task
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    """Meta Data"""
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """Login Form View"""
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
