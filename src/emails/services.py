from .models import Email, EmailVerificationEvent

def verify_email(email):
    qs = Email.objects.filter(email=email, active=False)
    return qs.exists()


def start_verification_event(email):
    email_obj, created = Email.objects.get_or_create(email=email)
    obj = EmailVerificationEvent.objects.create(
        parent=email_obj,
        email=email
    )
    # send an verification email
    return obj