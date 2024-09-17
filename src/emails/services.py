from django.conf import settings
from django.core.mail import send_mail
from .models import Email, EmailVerificationEvent

EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def verify_email(email):
    qs = Email.objects.filter(email=email, active=False)
    return qs.exists()

def get_verification_email_msg(verification_instance, as_html=False):
    if not isinstance(verification_instance, EmailVerificationEvent):
        return None
    if as_html:
        return f"<h1>{verification_instance.id}</h1>"
    return f"{verification_instance.id}"


def start_verification_event(email):
    email_obj, created = Email.objects.get_or_create(email=email)
    obj = EmailVerificationEvent.objects.create(
        parent=email_obj,
        email=email
    )
    sent = send_verification_email(obj.id)
    return obj, sent

# celery task -> background task
def send_verification_email(verify_obj_id,):
    verify_obj = EmailVerificationEvent.objects.get(id=verify_obj_id)
    email = verify_obj.email
    subject = "Verify your email"
    text_msg = get_verification_email_msg(verify_obj, as_html=False)
    text_html = get_verification_email_msg(verify_obj, as_html=True)
    from_user_email_addr = EMAIL_HOST_USER
    to_user_email = email
    # send an verification email
    return send_mail(
        subject,
        text_msg,
        from_user_email_addr,
        [to_user_email],
        fail_silently=False,
        html_message=text_html
    )