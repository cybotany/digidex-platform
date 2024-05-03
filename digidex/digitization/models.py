import uuid

from django.db import models

from wagtail.fields import RichTextField

from accounts.models import UserProfilePage
from inventory.models import UserDigitizedObjectInventoryPage, UserDigitizedObject


class DigitizedObject(models.Model):
    """
    Base class for digitized objects, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object.
        uuid (UUIDField): The unique identifier for the digitized object.
        description (RichTextField): A detailed description of the digitized object.
        created_at (DateTimeField): The date and time the digitized object was created.
        last_modified (DateTimeField): The date and time the digitized object was last modified.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=False
    )
    description = RichTextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def create_user_association(self, user):
        """
        Create a user association with the digitized object.

        Args:
            user (User): The user to associate with the digitized object.

        Returns:
            UserDigitizedObject: The user digitized object association.
        """
        user_profile_page = UserProfilePage.objects.get(profile=user.profile)
        user_inventory_page = UserDigitizedObjectInventoryPage.objects.child_of(user_profile_page).first()
        user_association = UserDigitizedObject.objects.create(
            parent=user_inventory_page,
            digit=self
        )
        return user_association
