from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[validate_password])
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput(), validators=[validate_password])

    class Meta:
        model = User
        fields = ("username", "email", "password", "password_confirm")
    
    
    def clean(self):
        password = self.cleaned_data["password"]
        password_confirm = self.cleaned_data["password_confirm"]

        if password != password_confirm:
            raise ValidationError(message={"password":"Пароли не совпали!"}) 

        return super().clean()
        

class ChangePasswordForm(forms.Form):
    real_password = forms.CharField(max_length=50)
    new_password = forms.CharField(max_length=50, validators=[validate_password])
    new_password_confirm = forms.CharField(max_length=50, validators=[validate_password])

    def clean(self):
        password = self.cleaned_data["new_password"]
        password_confirm = self.cleaned_data["new_password_confirm"]

        if password != password_confirm:
            raise ValidationError(message={"new_password":"Пароли не совпали!"}) 

        return super().clean()
