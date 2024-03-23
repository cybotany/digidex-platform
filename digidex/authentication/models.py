import uuid
from django.db import transaction
from django.contrib.auth.models import AbstractUser
# Project specific imports
from base.utils import validators
from base.fields import django_fields

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
    username = django_fields.BaseCharField(
        max_length=32,
        unique=True,
        validators=[validators.validate_username],
        help_text="Required. 32 characters or fewer. Letters, digits and dashes only.",
    )
    uuid = django_fields.BaseUUIDField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        verbose_name="User UUID",
        help_text="The universal unique identifier associated with each User."
    )
    email_confirmed = django_fields.BaseBooleanField(
        default=False,
        help_text='Indicates whether the user has confirmed their email address.'
    )

    def __str__(self):
        return self.username

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        super().save(*args, **kwargs)
