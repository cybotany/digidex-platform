from django.db import models
from django.core.mail import send_mail, BadHeaderError
import logging

logger = logging.getLogger(__name__)

class EmailLog(models.Model):
    REASONS = (
        ('email_verification', 'Email Verification'),
        ('password_reset', 'Password Reset'),
        ('contact_us', 'Contact Us Form'),
    )

    reason = models.CharField(
        max_length=100,
        choices=REASONS,
        help_text='The reason why the email was sent.'
    )
    to_email = models.EmailField(
        max_length=255,
        help_text='The email address the email was sent to.'
    )
    from_email = models.EmailField(
        max_length=255,
        help_text='The email address the email was sent from.'
    )
    subject = models.CharField(
        max_length=255,
        help_text='Subject of the email.'
    )
    body = models.TextField(
        help_text='Text content of the email.'
    )
    html_content = models.TextField(
        blank=True,
        null=True,
        help_text='HTML content of the email.'
    )
    status = models.CharField(
        max_length=50,
        default='sent',
        help_text='Status of the email (sent, failed, etc.)'
    )
    date_sent = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time the email was sent.'
    )
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='email_logs',
        help_text='The user associated with this email, if applicable.')

    class Meta:
        ordering = ['-date_sent']
        verbose_name = 'Email Log'
        verbose_name_plural = 'Email Logs'

    def __str__(self):
        return f"Email to {self.to_email} on {self.date_sent.strftime('%Y-%m-%d %H:%M')}"

    @classmethod
    def create_and_send_email(cls, to_email, from_email, subject, body, reason, user=None):
        email_log = cls(
            to_email=to_email,
            from_email=from_email,
            subject=subject,
            body=body,
            reason=reason,
            user=user,
            status='sent'
        )
        email_log.save()

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=from_email,
                recipient_list=[to_email],
                fail_silently=False,
            )
        except (BadHeaderError, Exception) as e:
            # Update the log to indicate the failure
            email_log.status = 'failed'
            email_log.save()

            logger.warning(f"Email failed: {e}")
            # Reraise the exception if you want calling code to handle it
            raise

        return email_log