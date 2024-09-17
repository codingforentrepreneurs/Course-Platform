from django import forms 

from .models import Email


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ['email']