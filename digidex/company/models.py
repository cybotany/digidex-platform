from django import forms
from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalManyToManyField
from wagtail.models import Page
from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


BaseUser = get_user_model()


@register_snippet
class TeamMember(models.Model):
    user = models.ForeignKey(
        BaseUser,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    role = models.CharField(
        max_length=255,
        blank=True
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('user'),
        FieldPanel('role'),
    ]

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'company team members'


class CompanyIndexPage(Page):
    parent_page_types = ["home.HomePage"]

    intro = models.CharField(
        max_length=250,
        blank=True
    )
    team_members = ParentalManyToManyField(
        TeamMember,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('team_members', widget=forms.CheckboxSelectMultiple),
    ]
