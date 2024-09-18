from django.conf import settings
from django.shortcuts import render

from emails import services as emails_services
from emails.models import Email, EmailVerificationEvent
from emails.forms import EmailForm


def login_logout_template_view(request):
    return render(request, "auth/login-logout.html", {})

EMAIL_ADDRESS = settings.EMAIL_ADDRESS
def home_view(request, *args, **kwargs):
    template_name = "home.html"
    # request POST data
    print(request.POST)
    form = EmailForm(request.POST or None)
    context = {
        "form": form,
        "message": ""
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = emails_services.start_verification_event(email_val)
        print(obj)
        context['form'] = EmailForm()
        context['message'] = f"Succcess! Check your email for verification from {EMAIL_ADDRESS}"
    else:
        print(form.errors) 
    print('email_id', request.session.get('email_id'))
    return render(request, template_name, context)