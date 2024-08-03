from django import forms
from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.models import Page, Orderable, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


BaseUser = get_user_model()

class TeamMemberRole(RevisionMixin, models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'role'
        verbose_name_plural = 'roles'


class TeamMember(Orderable):
    team = ParentalKey(
        "company.Team",
        null=True,
        blank=True,
        related_name='members',
        on_delete=models.CASCADE
    )
    user = models.OneToOneField(
        BaseUser,
        null=True,
        blank=True,
        related_name='team_profile',
        on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        TeamMemberRole,
        null=True,
        blank=True,
        related_name='team_members',
        on_delete=models.SET_NULL
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'


class Team(RevisionMixin, PreviewableMixin, TranslatableMixin, ClusterableModel):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def get_preview_template(self, request, mode_name):
        return "company/previews/team.html"

    class Meta(TranslatableMixin.Meta):
        verbose_name = 'team'
        verbose_name_plural = 'teams'


class CompanyIndexPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = []

    intro = models.CharField(
        max_length=255,
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
    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
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
        members = []
        for member in self.team.members.all():
            user = member.user
            role = member.role

            members.append({
                'name': f'{user.first_name} {user.last_name}',
                'role': role.name,
                'image': member.image,
            })
        return {
            'members': members,
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
        FieldPanel('team'),
    ]
