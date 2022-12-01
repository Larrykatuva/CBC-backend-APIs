import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


class EmailThreading(threading.Thread):
    """Email threading for faster processing"""
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class Email:
    """
    Email class to handle all email operations
    """

    @staticmethod
    def send_mail(
            email_subject: str,
            email_body: str,
            send_to: list
    ) -> None:
        """Sending email without a styled template"""
        email = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            send_to,
        )
        EmailThreading(email).start()

    @staticmethod
    def send_email_template(
            email_subject: str,
            email_body: str,
            send_to: list,
            template_name: str
    ) -> None:
        """Sending email with a styled template"""
        html_template = template_name
        html_message = render_to_string(
            html_template,
            {'content': email_body, }
        )
        email = EmailMessage(
            email_subject,
            html_message,
            settings.EMAIL_HOST_USER,
            send_to,
        )
        email.content_subtype = 'html'
        EmailThreading(email).start()

