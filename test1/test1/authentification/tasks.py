from __future__ import absolute_import, unicode_literals
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from celery.decorators import task
from celery import shared_task

from .tokens import account_activation_token

@task(name="send_email")
def send_confirmation_email(domain, user_id, email):
    user = get_user_model().objects.get(pk=user_id)
    mail_subject = 'Account confirmation'
    message = render_to_string('confirmation_email.html', {
        'username': user.username,
        'domain': domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    to_email = [email]
    email = EmailMessage(
        subject=mail_subject,
        body=message,
        to=to_email)
    email.send()
