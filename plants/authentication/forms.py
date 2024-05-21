from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.moddelForm):
    password_conf = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    class Meta:
        Model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_conf']