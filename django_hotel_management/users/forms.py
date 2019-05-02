from django import forms
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
#    phonenumber = PhoneField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
