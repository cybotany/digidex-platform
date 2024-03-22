from logging import getLogger
import uuid
from django.db import models, transaction
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
# Project specific imports
from cms.utils import  validators

logger = getLogger(__name__)

class DigiDexUser(AbstractUser):
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
    username = models.CharField(
        max_length=32,
        unique=True,
        validators=[validators.validate_username],
        help_text="Required. 32 characters or fewer. Letters, digits and dashes only.",
    )
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track the original username to detect changes
        self.__original_username = self.username
        # Track if the instance is new
        self.__original_new_user = self.pk is None

    def __str__(self):
        return self.username

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)

        if self.__original_new_user:
            try:
                self.send_verification_email()
            except Exception as e:
                logger.error(f'Error sending verification email: {e}')
                raise

    def send_verification_email(self):
        token = PasswordResetTokenGenerator().make_token(self)
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        base_url = reverse('verify-user', kwargs={'uidb64': uid, 'token': token})
        full_url = f'{settings.SITE_HOST}{base_url}'

        try:
            send_mail(
                subject='Verify your email',
                message=f'Please click the following link to verify your email and complete the signup process:\n{full_url}',
                from_email='no-reply@digidex.app',
                recipient_list=[self.email],
                fail_silently=False,
            )
        except (BadHeaderError, Exception) as e:
            logger.warning(f"Email failed: {e}")
            raise
