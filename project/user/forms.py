""" Inherit User Forms to add fields """
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    """ Class to inherit userCreationForm and add a field """

    username = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username'),
                'class': 'form-control'
            }
        ),
    )
    first_name = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('First name'),
                'class': 'form-control'
            }
        ),
    )
    last_name = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Last name'),
                'class': 'form-control'
            }
        ),
    )
    email = forms.EmailField(
        max_length=250,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'class': 'form-control'
            }
        ),
    )
    password1 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password'),
                'class': 'form-control'
            }
        ),
    )
    password2 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password confirmation'),
                'class': 'form-control'
            }
        ),
    )
    subscribed = forms.BooleanField(
        required=False,
        label=_('be informed of a V2 of the site ?'),
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'subscribed'
        ]


class LoginForm(AuthenticationForm):
    """ Class to inherit AuthenticationForm to display in wiew """

    username = forms.EmailField(
        max_length=250,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'class': 'form-control'
            }
        ),
    )

    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _('Password'),
                'class': 'form-control'
            }
        ),
    )
