from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.http import urlencode
from django.conf import settings
from django.core.mail import send_mail
import uuid


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
        base_url = reverse('accounts:verify-email')
        query_string = urlencode({'token': token, 'email': self.email})
        full_url = f'http://{settings.SITE_HOST}{base_url}?{query_string}'

        send_mail(
            'Verify your email',
            f'Please click the following link to verify your email: {full_url}',
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.is_active = False
        super().save(*args, **kwargs)
        if not self.pk:
            self.send_verification_email()
