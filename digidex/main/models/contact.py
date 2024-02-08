from django.db import models, transaction
from django.utils.timezone import now
from datetime import timedelta
from digidex.accounts.models import EmailLog

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

    def send_contact_form_email(self):
        """
        Sends an email to the user after a contact form submission.
        """
        # Use EmailLog to create and send the email
        EmailLog.create_and_send_email(
            to_email=self.email,
            from_email='no-reply@digidex.app',
            subject='Thank you for contacting us',
            body='We have received your message and will get back to you soon.',
            reason='contact_us',
            user=None
        )

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.send_contact_form_email()
        except Exception as e:
            raise e

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