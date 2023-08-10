from django.core.mail import send_mail
from django.conf import settings

def send_review_email(message, recipient_list):
    
    subject = 'Thanks For Review'
    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, recipient_list)
