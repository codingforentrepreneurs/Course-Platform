from django import forms 

from . import css
from .models import Email, EmailVerificationEvent


class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs = {
                "id": "email-login-input",
                "class": css.EMAIL_FIELD_CSS,
                "placeholder": "your email login"
            }
        )
    )
    class Meta:
        model = EmailVerificationEvent
        fields = ['email']