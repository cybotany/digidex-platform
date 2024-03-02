import uuid
from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import JSONField

class _Digitization(models.Model):
    """
    Abstract base model for digitized entities.

    Attributes:
        uuid (UUIDField): The unique identifier associated with each Digit.
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        is_public (BooleanField): Indicates if the digit should be publicly visible to the public or private. Digit is private by default.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="UUID of the digitized entity",
        help_text="The unique identifier associated with the digitized entity."
    )
    name = models.CharField(
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized entity."
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="A short description of the digitized entity."
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the digitized entity should be publicly visible. Is set to private by default.'
    )
    metadata = JSONField(
        default=dict,
        blank=True,
        help_text="A JSON field for storing arbitrary metadata."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the digitized entity instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the digitized entity instance was last modified."
    )

    @property
    def entity_type(self):
        """
        A property to dynamically retrieve the type of the digitized entity.
        """
        return self.__class__.__name__.lower()

    def _get_parent_details(self):
        """
        Returns information about the grouping's owner, including the URL to their profile 
        and their username.
        
        Returns:
        A dictionary containing the 'url' and 'name' of the grouping's owner.
        """
        pass

    def _get_view_details(self):
        """
        Subclasses should return the URL name associated with the model's detail view.
        """
        raise NotImplementedError("Subclasses must define a `_get_view_details` method.")

    def _pre_delete(self, *args, **kwargs):
        """
        Hook method for custom pre-delete logic in subclasses.
        """
        pass

    def _post_delete(self, *args, **kwargs):
        """
        Hook method for custom post-delete logic in subclasses.
        """
        pass

    def pre_delete(self, *args, **kwargs):
        """
        Hook method for custom pre-delete logic in subclasses.
        """
        self._pre_delete(*args, **kwargs)

    def post_delete(self, *args, **kwargs):
        """
        Hook method for custom post-delete logic in subclasses.
        """
        self._post_delete

    def delete(self, *args, **kwargs):
        """
        Overrides the default delete method to include pre-delete and post-delete hooks.
        """
        self.pre_delete(*args, **kwargs)
        super().delete(*args, **kwargs)
        self.post_delete(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the URL to view the details of this digitized entity.
        Utilizes the `_get_view_details` method for dynamic URL name retrieval.
        """
        return reverse(self._get_view_details())

    class Meta:
        abstract = True
        ordering = ['-created_at']
        