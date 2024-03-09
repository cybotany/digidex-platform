from logging import getLogger
import uuid
from django.db import models, transaction
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import slugify
from django.conf import settings
# Project specific imports
from cms.utils import cms_storage
from cms.utils import validators

logger = getLogger(__name__)

def profile_avatar_directory_path(instance, filename):
    return f'profile_{instance.id}/avatar.jpeg'

class DigidexUser(AbstractUser):
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
        - slug (SlugField): A slugified version of the username for URL usage.
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
    slug = models.SlugField(
        unique=True,
        max_length=255,
        editable=False,
        db_index=True,
        help_text="Slugified version of the username for URL usage."
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
        if not self.slug or self.username != self.__original_username:
            base_slug = slugify(self.username)
            unique_slug = base_slug
            num = 1
            while DigidexUser.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{base_slug}-{num}'
                num += 1
            self.slug = unique_slug

        super().save(*args, **kwargs)

        # Send verification email for new users
        if self.__original_new_user:
            try:
                self.send_verification_email()
            except Exception as e:
                raise Exception(f'Error sending verification email: {e}')

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
            # Reraise the exception if you want calling code to handle it
            raise


class DigidexProfile(models.Model):
    """
    User profile model for storing additional user information.

    Fields:
        user (OneToOneField): A one-to-one reference to the User model.
        bio (TextField): A text field for user biography, maximum length 500 characters.
        location (CharField): A char field for user location, maximum length 30 characters.
        avatar (ImageField): An image field for user's profile picture.
        is_public (BooleanField): A boolean field to determine if the profile is public or private. Profile is private by default.
        created_at (DateTimeField): The date and time when the profile was created.
        last_modified (DateTimeField): The date and time when the profile was last modified.
    """
    user = models.OneToOneField(
        DigidexUser,
        on_delete=models.CASCADE,
        help_text='The user associated with this profile.'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        help_text='A short biography of the user.'
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        help_text='The location of the user.'
    )
    avatar = models.ImageField(
        upload_to=profile_avatar_directory_path,
        storage=cms_storage.PublicMediaStorage, # PublicMediaStorage()?
        null=True,
        blank=True,
        help_text='The avatar image of the profile.'
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the profile should be publicly visible to the public or private. Profile is private by default.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the profile was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the profile was last modified."
    )

    def __str__(self):
        """
        Returns a string representation of the user's profile.

        Returns:
            str: A string in the format "<username>'s Profile".
        """
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        """
        Get the URL to view the details of this profile.

        Returns:
            str: The URL to view the details of this profile.
        """
        return reverse('profile', kwargs={'username_slug': self.user.username_slug})

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
