from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class RegisterForm(UserCreationForm):

    is_editor = forms.BooleanField(
        required=False,
        label="Register as Editor"
    )

    class Meta:
        model = UserProfile
        fields = ["username", "email", "is_editor"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            "username": "Enter Username",
            "email": "Enter email",
            "password1": "Enter password",
            "password2": "Confirm password"
        }

        for field_name, placeholder in labels.items():
            self.fields[field_name].widget.attrs.update({
                "class": "input-field",
                "placeholder": placeholder
            })