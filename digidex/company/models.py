from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from base.models.body import BasePage

class CompanyIndexPage(BasePage):
    parent_page_types = ["home.HomePage"]

    # About section fields
    about_vision = models.TextField(blank=True, null=True)
    about_mission = models.TextField(blank=True, null=True)
    about_values = models.TextField(blank=True, null=True)

    # Quote section fields
    quote_heading_title = models.CharField(max_length=255, blank=True, null=True)
    quote_member_name = models.CharField(max_length=255, blank=True, null=True)
    quote_member_role = models.CharField(max_length=255, blank=True, null=True)
    quote_member_signature = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    # Team section fields
    team_heading_subtitle = models.CharField(max_length=255, blank=True, null=True)
    team_heading_title = models.CharField(max_length=255, blank=True, null=True)
    team_member_name = models.CharField(max_length=255, blank=True, null=True)
    team_member_role = models.CharField(max_length=255, blank=True, null=True)
    team_member_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = BasePage.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_vision'),
            FieldPanel('about_mission'),
            FieldPanel('about_values'),
        ], heading="About Section"),
        MultiFieldPanel([
            FieldPanel('quote_heading_title'),
            FieldPanel('quote_member_name'),
            FieldPanel('quote_member_role'),
        ], heading="Quote Section"),
        MultiFieldPanel([
            FieldPanel('team_heading_subtitle'),
            FieldPanel('team_heading_title'),
            FieldPanel('team_member_name'),
            FieldPanel('team_member_role'),
        ], heading="Team Section"),
    ]
