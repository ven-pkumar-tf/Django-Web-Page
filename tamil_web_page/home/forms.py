# home/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    user_role = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin')])

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data
