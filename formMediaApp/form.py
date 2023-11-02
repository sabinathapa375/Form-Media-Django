from .models import Registration
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Registration
        fields = ["username","email","password1","password2","phone","picture","document"]