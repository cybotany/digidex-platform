import uuid

from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from wagtail.models import Page, Collection
from wagtail.admin.panels import FieldPanel


class Trainer(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"

    class Meta:
        verbose_name = _('trainer')
        verbose_name_plural = _('trainers')


class TrainerIndexPage(Page):
    trainer = models.OneToOneField(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='page'
    )
    collection = models.OneToOneField(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('trainer'),
        FieldPanel('collection'),
    ]

    def create_slug(self):
        return slugify(self.trainer.user.username)

    def set_slug(self):
        self.slug = self.create_slug()

    def get_parent_collection(self):
        parent = Collection.get_first_root_node()
        parent_children = parent.get_children()
        try:
            collection = parent_children.get(name='Trainers')
        except Collection.DoesNotExist:
            collection = parent.add_child(name="Trainers")
        return collection

    @transaction.atomic
    def create_collection(self):
        parent = self.get_parent_collection()
        uuid = str(self.trainer.uuid)
        children = parent.get_children()
        try:
            trainer_collection = children.get(name=uuid)
        except Collection.DoesNotExist:
            trainer_collection = parent.add_child(name=uuid)
        return trainer_collection

    def get_documents(self):
        return get_document_model().objects.filter(collection=self.collection)

    def get_images(self):
        return get_image_model().objects.filter(collection=self.collection)

    def is_owner(self, user):
        return user == self.trainer.user

    def save(self, *args, **kwargs):
        if not self.slug:
            self.set_slug()
        if not self.collection:
            self.collection = self.create_collection()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.trainer.__str__()}'s page"

    class Meta:
        verbose_name = _('trainer page')
        verbose_name_plural = _('trainer pages')
