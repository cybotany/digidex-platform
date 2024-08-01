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
        FieldPanel('image'),
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
    our_mission = models.TextField(
        blank=True
    )
    our_vision = models.TextField(
        blank=True
    )
    our_values = models.TextField(
        blank=True
    )
    team_subtitle = models.CharField(
        max_length=255,
        blank=True
    )
    team_heading = models.CharField(
        max_length=255,
        blank=True
    )
    team_members = ParentalManyToManyField(
        TeamMember,
        blank=True
    )

    def get_body_header(self):
        return {
            'title': self.title,
            'intro': self.intro if self.intro else 'Needs to be defined'
        }

    def get_about_us(self):
        return {
            'mission': self.our_mission if self.our_mission else 'Needs to be defined',
            'vision': self.our_vision if self.our_vision else 'Needs to be defined',
            'values': self.our_values if self.our_values else 'Needs to be defined'
        }

    def get_our_team(self):
        return {
            'subtitle': self.team_subtitle if self.team_subtitle else 'The Team',
            'heading': self.team_heading if self.team_heading else 'Meet the people behind the company',
            'members': self.team_members.all()
        }

    def get_context(self, request):
        context = super().get_context(request)
        context['header'] = self.get_body_header()
        context['about'] = self.get_about_us()
        context['team'] = self.get_our_team()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        MultiFieldPanel(
            [
                FieldPanel('our_mission'),
                FieldPanel('our_vision'),
                FieldPanel('our_values'),
            ],
            heading="About Us Section"
        ),
        MultiFieldPanel(
            [
                FieldPanel('our_mission'),
                FieldPanel('our_vision'),
                FieldPanel('team_members', widget=forms.CheckboxSelectMultiple),
            ],
            heading="Our Team Section"
        ),
    ]
