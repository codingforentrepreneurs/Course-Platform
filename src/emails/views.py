from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import services

from .forms import EmailForm

EMAIL_ADDRESS = settings.EMAIL_ADDRESS

def email_token_login_view(request):
    if not request.htmx:
        return redirect('/')
    template_name = "emails/hx/form.html"
    form = EmailForm(request.POST or None)
    context = {
        "form": form,
        "message": ""
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = services.start_verification_event(email_val)
        context['form'] = EmailForm()
        context['message'] = f"Succcess! Check your email for verification from {EMAIL_ADDRESS}"
    else:
        print(form.errors) 
    return render(request, template_name, context)

# Create your views here.
def verify_email_token_view(request, token, *args, **kwargs):
    did_verify, msg, email_obj = services.verify_token(token)
    if not did_verify:
        try:
            del request.session['email_id']
        except:
            pass
        messages.error(request, msg)
        return redirect("/login/")
    messages.success(request, msg)
    # django -> request.session.get('email_id)
    request.session['email_id'] = f"{email_obj.id}"
    next_url = request.session.get('next_url') or "/"
    if not next_url.startswith("/"):
        next_url = "/"
    return redirect(next_url)