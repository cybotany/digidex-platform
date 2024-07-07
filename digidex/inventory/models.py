import uuid

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from treebeard.mp_tree import MP_Node, MP_NodeManager, MP_NodeQuerySet

from wagtail.models import (
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    Collection
)
from wagtail.query import TreeQuerySet
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from nearfieldcommunication.models import NearFieldCommunicationTag


class InventoryQuerySet(TreeQuerySet):
    def get_min_depth(self):
        return self.aggregate(models.Min("depth"))["depth__min"] or 2

    def get_indented_choices(self):
        """
        Return a list of (id, label) tuples for use as a list of choices in a inventory chooser
        dropdown, where the label is formatted with get_indented_name to provide a tree layout.
        The indent level is chosen to place the minimum-depth inventory at indent 0.
        """
        min_depth = self.get_min_depth()
        return [
            (inventory.pk, inventory.get_indented_name(min_depth, html=True))
            for inventory in self
        ]


class BaseInventoryManager(models.Manager):
    def get_queryset(self):
        return InventoryQuerySet(self.model).order_by("path")


InventoryManager = BaseInventoryManager.from_queryset(InventoryQuerySet)


class BaseInventory(
    WorkflowMixin,
    PreviewableMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    SpecificMixin,
    MP_Node
):
    """
    Base class for all inventory items, categories, and notes.
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    slug = models.SlugField(
        max_length=255,
        db_index=True
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='+',
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    body = RichTextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    objects = InventoryManager()

    node_order_by = ["slug"]


    content_panels = [
        FieldPanel('name'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True
    

class Inventory(BaseInventory):
    """
    Acts as the index for all user-specific inventory members.
    """

    def __str__(self):
        return f"{self.name}'s Inventory"

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventories")
        constraints = [
            models.UniqueConstraint(
                fields=('translation_key', 'locale'),
                name='unique_translation_key_locale_inventory_inventory'
            )
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def setup_collection(self, username=None):
        """
        Creates a new collection
        """
        if not username:
            username = self.user.username.title()
        
        root_collection = Collection.get_first_root_node()
        try:
            user_collection = root_collection.objects.get(name=username)
        except Collection.DoesNotExist:
            user_collection = root_collection.add_child(name=username)
        return user_collection

    def setup_inventory(self):
        """
        Creates a new inventory
        """
        if not self.inventory:
            user_name = self.user.username.title()
            user_slug = slugify(user_name)

            root_nodes = Inventory.objects.root_nodes()
            user_inventory = root_nodes.get(slug=user_slug)

            if not user_inventory.exists():
                user_collection = self.setup_collection(username=user_name)
                user_inventory = Inventory(
                    name=user_name,
                    owner=self.user,
                    slug=user_slug,
                    collection=user_collection
                )
    
            user_inventory = Inventory.add_root(instance=user_inventory)
            self.inventory = user_inventory
        return self.inventory

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")


class Category(Inventory):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Item(Inventory):
    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")


class Link(NearFieldCommunicationTag):
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.SET_NULL,
        related_name='+',
        null=True
    )

    def __str__(self):
        if self.inventory:
            return f"{self} for {self.inventory}"
        return f"{self} available for mapping"

    def get_url(self):
        """
        Constructs the absolute URL to view this specific NFC tag.

        Returns:
            A URL path as a string.
        """
        return reverse('nfc:route_nfc', kwargs={'link_uuid': self.uuid})

    class Meta:
        verbose_name = _("link")
        verbose_name_plural = _("links")
