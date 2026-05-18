from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Profile

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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label=_("Email Address"))

    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-brand-500 sm:text-sm sm:leading-6'
            })


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Tell us a bit about yourself...',
        })
    )

    class Meta:
        model = Profile
        fields = ("bio", "avatar")
        widgets = {
            'avatar': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({
            'class': 'block w-full rounded-md border-0 py-1.5 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-brand-500 sm:text-sm sm:leading-6'
        })
        self.fields['avatar'].widget.attrs.update({
            'class': 'block w-full text-sm text-gray-900 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-brand-50 file:text-brand-500 hover:file:bg-brand-100 cursor-pointer'
        })
