from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalManyToManyField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
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

    panels = [
        FieldPanel('user'),
    ]

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'company team members'


class CompanyPage(Page):
    parent_page_types = ["home.HomePage"]

    team_members = ParentalManyToManyField(
        TeamMember,
        blank=True
    )

