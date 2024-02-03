from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta

class Contact(models.Model):
    """
    Contact model for storing contact form submissions.

    Fields:
        name (CharField): The name of the person submitting the contact form.
        email (EmailField): The email address of the person submitting the form.
        message (TextField): The message content from the contact form.
        response_received (BooleanField): Whether this contact instance has received a response for the message.
        created_at (DateTimeField): The date and time when the contact form was submitted.
    """
    name = models.CharField(
        max_length=256,
        verbose_name="Name",
        help_text="The name of the person submitting the contact form."
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="The email address of the person submitting the contact form."
    )
    message = models.TextField(
        verbose_name="Message",
        help_text="The message content from the contact form."
    )
    response_received = models.BooleanField(
        default=False,
        verbose_name="Response Received",
        help_text="Whether this contact instance has received a response for the message."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the contact form was submitted."
    )

    def __str__(self):
        """
        Returns a string representation of a contact form submission.

        Returns:
            str: A string in the format "Contact submission from <name>".
        """
        return f"Contact submission from {self.name}"

    def send_email(self):
        """
        Sends an email to the user after a contact form submission.
        """
        send_mail(
            subject="Thank you for contacting us",
            message="We have received your message and will get back to you soon.",
            from_email='no-reply@digidex.app',
            recipient_list=[self.email],
            fail_silently=False,
        )

    @classmethod
    def get_pending_responses_summary(cls):
        # Filter for contacts that haven't received a response
        contacts = cls.objects.filter(response_received=False)

        # Define the time thresholds
        one_day_ago = now() - timedelta(days=1)
        one_week_ago = now() - timedelta(weeks=1)
        one_month_ago = now() - timedelta(weeks=4)

        # Mutually Exclusive Group contacts based on submission duration
        day_old_contacts = contacts.filter(created_at__gte=one_day_ago)
        week_old_contacts = contacts.filter(created_at__gte=one_week_ago, created_at__lt=one_day_ago)
        month_old_contacts = contacts.filter(created_at__gte=one_month_ago, created_at__lt=one_week_ago)

        # Build and return the summary
        summary = {
            'day_old': day_old_contacts.count(),
            'week_old': week_old_contacts.count(),
            'month_old': month_old_contacts.count()
        }
        return summary