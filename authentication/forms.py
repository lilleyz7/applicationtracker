from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['first_name','email','password1','password2'] 