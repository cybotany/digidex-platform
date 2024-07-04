from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from wagtail.models import CollectionMember, ReferenceIndex
from wagtail.search import index
from wagtail.search.queryset import SearchableQuerySetMixin


class NoteQuerySet(SearchableQuerySetMixin, models.QuerySet):
    pass


class AbstractNote(CollectionMember, index.Indexed, models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("title")
    )
    entry = models.TextField(
        verbose_name=_("entry"),
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True
    )
    submitted_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("submitted by user"),
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
    )
    submitted_by_user.wagtail_reference_index_ignore = True

    tags = TaggableManager(
        help_text=None,
        blank=True,
        verbose_name=_("tags")
    )

    objects = NoteQuerySet.as_manager()

    search_fields = CollectionMember.search_fields + [
        index.SearchField("title", boost=10),
        index.SearchField("entry", boost=1),
        index.AutocompleteField("title"),
        index.FilterField("title"),
        index.RelatedFields(
            "tags",
            [
                index.SearchField("name", boost=10),
                index.AutocompleteField("name"),
            ],
        ),
        index.FilterField("submitted_by_user"),
    ]

    def __str__(self):
        return self.title

    @property
    def url(self):
        return reverse("wagtaildocs_serve", args=[self.id, self.filename])

    def get_usage(self):
        return ReferenceIndex.get_grouped_references_to(self)

    @property
    def usage_url(self):
        return reverse("wagtaildocs:document_usage", args=(self.id,))

    def is_editable_by_user(self, user):
        from wagtail.documents.permissions import permission_policy

        return permission_policy.user_has_permission_for_instance(user, "change", self)


    class Meta:
        abstract = True
        verbose_name = _("note")
        verbose_name_plural = _("notes")


class Note(AbstractNote):
    admin_form_fields = ("title", "entry", "collection", "tags")

    class Meta(AbstractNote.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
