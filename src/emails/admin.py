from django.contrib import admin

# Register your models here.
from .models import Email, EmailVerificationEvent

admin.site.register(Email)
admin.site.register(EmailVerificationEvent)