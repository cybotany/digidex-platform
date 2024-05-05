import uuid
from django.db import models

from inventory.models import UserDigitizedObject, UserDigitizedObjectPage

class DigitizedObject(models.Model):
    """
    Base class for digitized objects, providing common attributes.

    Attributes:
        name (CharField): The name of the digitized object.
        uuid (UUIDField): The unique identifier for the digitized object.
        description (TextField): A detailed description of the digitized object.
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
        blank=False,
        help_text="Enter the name of the digitized object."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Provide a detailed description of the object."
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name}"

    def set_user_association(self, user):
        return UserDigitizedObject.objects.create(user=user, digit=self)

    def get_user_association(self):
        return UserDigitizedObject.objects.get(digit=self)

    def get_user_association(self):
        return UserDigitizedObject.objects.get(digit=self)

    def get_associated_page_url(self):
        try:
            user_digit = self.get_user_association()
            user_digit_page = user_digit.detail_page 
            return user_digit_page.url if user_digit_page else None
        except UserDigitizedObject.DoesNotExist:
            return None
        except UserDigitizedObjectPage.DoesNotExist:
            return None

class DigitizedObjectImage(models.Model):
    digit = models.ForeignKey(
        DigitizedObject,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+',
        help_text="Select an image to associate with the digitized object."
    )
    caption = models.CharField(
        blank=True,
        null=True,
        max_length=250,
        help_text="Enter a caption for the image."
    )
