import uuid
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.urls import reverse

class Digitize(models.Model):
    """
    Abstract base model for digitized entities within the Digit platform. This model provides
    core fields and functionality that are common across various types of digitized entities,
    such as plants, ecosystems, or any biodiversity elements managed by the platform.

    The model is designed to be extended by specific entity types, allowing for the
    addition of specialized fields and methods while retaining a consistent structure for
    attributes like identification, naming, visibility, and metadata handling.

    Attributes:
        uuid (UUIDField): A universally unique identifier for each instance, ensuring
                          global uniqueness across the platform.
        name (CharField): An optional human-readable name for easier identification
                          of the entity.
        description (TextField): An optional short text describing the entity.
        slug (SlugField): A unique, URL-friendly identifier for the entity, derived
                            from the name or other identifying attributes.
        is_public (BooleanField): A flag indicating whether the entity should be
                                  visible to the public. Defaults to False, making
                                  entities private by default.
        metadata (JSONField): A flexible field for storing arbitrary metadata about
                              the entity in JSON format.
        parent_type (ForeignKey): A reference to the ContentType of the parent object.
        parent_id (PositiveIntegerField): The ID of the parent object.
        parent_object (GenericForeignKey): A generic foreign key to the parent object.
        created_at (DateTimeField): The timestamp when the entity was created.
        last_modified (DateTimeField): The timestamp of the last modification to the entity.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="UUID",
        help_text="The unique identifier for the entity."
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="A human-readable name for the entity."
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="A short description of the entity."
    )
    slug = models.SlugField(
        max_length=255,
        help_text="A unique, URL-friendly identifier for the entity."
    )
    is_public = models.BooleanField(
        default=False,
        help_text="Indicates if the entity is publicly visible. Defaults to private."
    )
    metadata = JSONField(
        default=dict,
        blank=True,
        help_text="JSON-formatted metadata about the entity."
    )
    parent_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True
    )
    parent_id = models.PositiveIntegerField(
        null=True
    )
    parent_object = GenericForeignKey(
        'parent_type',
        'parent_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The creation time of the entity."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        help_text="The time of the last modification to the entity."
    )

    def __str__(self):
        return self.name or f"Digit {str(self.uuid)}"

    @property
    def entity_type(self):
        """
        Dynamically retrieves the type (class name) of the digitized entity. This can be
        used for logging, debugging, or implementing type-specific logic in a generic manner.

        Returns:
            str: A lowercase string representing the entity's class name.
        """
        return self.__class__.__name__.lower()

    def _get_api_url(self):
        """
        Returns the absolute URL to the entity's detail view in the API.
        Assumes the URL pattern name is 'entity-detail' and it expects a 'uuid' parameter.
        """

        return reverse(f'{self.entity_type}', kwargs={f'{self.entity_type}_uuid': self.uuid})

    def _get_slug_url(self):
        """
        Returns the absolute URL to the entity's detail view in the frontend.
        Assumes the URL pattern name is 'entity-detail' and it expects a 'slug' parameter.
        """
        return reverse(f'{self.entity_type}', kwargs={f'{self.entity_type}_slug': self.slug})

    def pre_delete(self, *args, **kwargs):
        """
        A hook method for custom pre-delete logic. Subclasses can override this method to
        perform actions before an entity is deleted from the database.

        The default implementation does nothing.
        """
        pass

    def post_delete(self, *args, **kwargs):
        """
        A hook method for custom post-delete logic. Subclasses can override this method to
        perform actions after an entity has been deleted from the database.

        The default implementation does nothing.
        """
        pass

    def delete(self, *args, **kwargs):
        """
        Overrides the default delete method to include hooks for pre-delete and post-delete
        actions. This allows for a clean way to extend deletion logic in subclasses.

        Any subclass overriding this method should ensure to call super().delete(*args, **kwargs)
        to preserve the hook execution order.
        """
        self.pre_delete(*args, **kwargs)
        super().delete(*args, **kwargs)
        self.post_delete(*args, **kwargs)

    def get_parent_details(self):
        """
        Returns information about the grouping's owner, including the URL to their profile 
        and their username.
        
        Returns:
        A dictionary containing the 'url' and 'name' of the grouping's owner.
        """
        raise NotImplementedError("Subclasses must implement `get_parent_details` method.")

    def get_absolute_url(self):
        """
        Returns the absolute URL to the detail view of this digitized entity using
        details provided by `get_absolute_url`. Handles both 'args' and 'kwargs' gracefully.

        Returns:
            str: The absolute URL to the entity's detail view.
        """
        raise NotImplementedError("Subclasses must implement `get_absolute_url` method.")

    class Meta:
        abstract = True
        