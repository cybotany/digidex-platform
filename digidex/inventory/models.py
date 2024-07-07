import uuid
import posixpath

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from treebeard.mp_tree import MP_Node
from modelcluster.models import ClusterableModel

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
from wagtail.fields import RichTextField
from wagtail.search import index

from inventory.queryset import InventoryQuerySet
from nearfieldcommunication.models import NearFieldCommunicationTag

from wagtail.models import BaseViewRestriction


class InventoryViewRestriction(BaseViewRestriction):
    inventory = models.ForeignKey(
        "Inventory",
        verbose_name=_("inventory"),
        related_name="view_restrictions",
        on_delete=models.CASCADE,
    )

    passed_view_restrictions_session_key = "passed_inventory_view_restrictions"

    class Meta:
        verbose_name = _("inventory view restriction")
        verbose_name_plural = _("inventory view restrictions")


class BaseInventoryManager(models.Manager):
    def get_queryset(self):
        return InventoryQuerySet(self.model).order_by("path")

InventoryManager = BaseInventoryManager.from_queryset(InventoryQuerySet)


class AbstractInventory(
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
    Abstract superclass for Page. According to Django's inheritance rules, managers set on
    abstract models are inherited by subclasses, but managers set on concrete models that are extended
    via multi-table inheritance are not. We therefore need to attach PageManager to an abstract
    superclass to ensure that it is retained by subclasses of Page.
    """

    objects = InventoryManager()

    class Meta:
        abstract = True
    

class Inventory(
    AbstractInventory,
    index.Indexed,
    ClusterableModel
):
    """
    Acts as the index for all user-specific inventory members.
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
    name = models.CharField(
        max_length=255,
        verbose_name=_("name")
    )
    body = RichTextField( 
        blank=True,
        null=True,
        verbose_name=_("body")
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='+',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    node_order_by = ["slug"]

    def __str__(self):
        return self.name

    def get_ancestors(self, inclusive=False):
        return Inventory.objects.ancestor_of(self, inclusive)

    def get_descendants(self, inclusive=False):
        return Inventory.objects.descendant_of(self, inclusive)

    def get_siblings(self, inclusive=True):
        return Inventory.objects.sibling_of(self, inclusive)

    def get_next_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__gte=self.path).order_by("path")

    def get_prev_siblings(self, inclusive=False):
        return (
            self.get_siblings(inclusive).filter(path__lte=self.path).order_by("-path")
        )

    def get_indented_name(self, indentation_start_depth=2, html=False):
        """
        Renders this Inventory's name as a formatted string that displays its hierarchical depth via indentation.
        If indentation_start_depth is supplied, the Inventory's depth is rendered relative to that depth.
        indentation_start_depth defaults to 2, the depth of the first non-Root Inventory.
        Pass html=True to get an HTML representation, instead of the default plain-text.

        Example text output: "    ↳ Pies"
        Example HTML output: "&nbsp;&nbsp;&nbsp;&nbsp;&#x21b3 Pies"
        """
        display_depth = self.depth - indentation_start_depth
        # A Inventory with a display depth of 0 or less (Root's can be -1), should have no indent.
        if display_depth <= 0:
            return self.name

        # Indent each level of depth by 4 spaces (the width of the ↳ character in our admin font), then add ↳
        # before adding the name.
        if html:
            # NOTE: &#x21b3 is the hex HTML entity for ↳.
            return format_html(
                "{indent}{icon} {name}",
                indent=mark_safe("&nbsp;" * 4 * display_depth),
                icon=mark_safe("&#x21b3"),
                name=self.name,
            )
        # Output unicode plain-text version
        return "{}↳ {}".format(" " * 4 * display_depth, self.name)

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


class InventoryCategory(Inventory):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class InventoryItem(Inventory):
    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")


class InventoryLink(NearFieldCommunicationTag):
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
