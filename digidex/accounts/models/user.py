import uuid
import logging
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from digidex.utils.models import EmailLog

logger = logging.getLogger(__name__)


class User(AbstractUser):
    """
    User model extending Django's AbstractUser. This model includes all fields
    from AbstractUser and additional fields for extended functionality.

    Default AbstractUser Fields:
        - username (CharField): The username for the user.
        - first_name (CharField): The first name of the user.
        - last_name (CharField): The last name of the user.
        - email (EmailField): The email address of the user.
        - password (CharField): The hashed password for the user.
        - groups (ManyToManyField): Group memberships.
        - user_permissions (ManyToManyField): Specific permissions for the user.
        - is_staff (BooleanField): Indicates if the user can access the admin site.
        - is_active (BooleanField): Indicates if the user's account is active.
        - is_superuser (BooleanField): Indicates if the user has all permissions.
        - last_login (DateTimeField): The last login date and time for the user.
        - date_joined (DateTimeField): The date and time the account was created.
    Extended Fields:
        - uuid (UUIDField): A universally unique identifier for the user.
        - email_confirmed (BooleanField): Indicates if the user has confirmed their email address.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        verbose_name="User UUID",
        help_text="The universal unique identifier associated with each User."
    )
    email_confirmed = models.BooleanField(
        default=False,
        help_text='Indicates whether the user has confirmed their email address.'
    )

    def __str__(self):
        return self.username

    def send_verification_email(self):
        token = PasswordResetTokenGenerator().make_token(self)
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        base_url = reverse('accounts:verify-email', kwargs={'uidb64': uid, 'token': token})
        full_url = f'{settings.SITE_HOST}{base_url}'

        # Use EmailLog to create and send the email
        EmailLog.create_and_send_email(
            to_email=self.email,
            from_email='no-reply@digidex.app',
            subject='Verify your email',
            body=f'Please click the following link to verify your email and complete the signup process:\n{full_url}',
            reason='email_verification',
            user=self
        )

    @transaction.atomic
    def save(self, *args, **kwargs):
        # Check if it's a new record
        new_user = self.pk is None
        # Save the user instance
        super().save(*args, **kwargs)
        # Send verification email for new users
        if new_user:
            try:
                self.send_verification_email()
            except Exception as e:
                raise
