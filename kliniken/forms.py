from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Booking


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']