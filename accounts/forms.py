from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_("Email Address"))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Email or Username"),
        max_length=254, 
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': "Enter Email or Username"}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': "Enter Password"}),
    )
