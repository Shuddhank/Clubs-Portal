from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class Signup_form(UserCreationForm):
    #password=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()
    class Meta:
        model = User
        fields=['email','username','password1','password2']

class Add_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['gender','ug']
