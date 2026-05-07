from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "input-field", "placeholder": "Enter email"}
        ),
    )

    class Meta:
        model = UserProfile
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Enter username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input-field", "placeholder": "Enter email"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "input-field", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "input-field", "placeholder": "Confirm password"}
        )
