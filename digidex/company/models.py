from base.models.body import BasePage
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
#from wagtail.images.edit_handlers import ImageChooserPanel

class CompanyIndexPage(BasePage):
    # About section fields
    about_vision = models.TextField(blank=True, null=True)
    about_mission = models.TextField(blank=True, null=True)
    about_values = models.TextField(blank=True, null=True)

    lottie_animation_1 = models.URLField(blank=True)
    lottie_animation_2 = models.URLField(blank=True)
    lottie_animation_2_blur = models.URLField(blank=True)

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

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_vision'),
            FieldPanel('about_mission'),
            FieldPanel('about_values'),
        ], heading="About Section"),
        MultiFieldPanel([
            FieldPanel('lottie_animation_1'),
            FieldPanel('lottie_animation_2'),
            FieldPanel('lottie_animation_2_blur'),
        ], heading="Lottie Animations"),
        MultiFieldPanel([
            FieldPanel('quote_heading_title'),
            FieldPanel('quote_member_name'),
            FieldPanel('quote_member_role'),
            #ImageChooserPanel('quote_member_signature'),
        ], heading="Quote Section"),
        MultiFieldPanel([
            FieldPanel('team_heading_subtitle'),
            FieldPanel('team_heading_title'),
            FieldPanel('team_member_name'),
            FieldPanel('team_member_role'),
            #ImageChooserPanel('team_member_image'),
        ], heading="Team Section"),
    ]

class CompanyPage(BasePage):
    pass