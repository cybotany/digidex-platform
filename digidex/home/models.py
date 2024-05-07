from django.db import models, transaction

from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page

from home.blocks import HomeStreamBlock


class HomePage(Page):
    hero_heading = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero Heading"
    )
    hero_paragraph = models.TextField(
        blank=True,
        verbose_name="Hero Paragraph"
    )
    hero_cta_text = models.CharField(
        blank=True,
        max_length=255,
        verbose_name="Hero CTA Text"
    )
    hero_cta_link = models.URLField(
        blank=True,
        verbose_name="Hero CTA Link"
    )
    body = StreamField(
        HomeStreamBlock(),
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
                FieldPanel('hero_cta_text'),
                FieldPanel('hero_cta_link'),
            ], heading="Hero Section"
        ),
        FieldPanel("body"),
    ]

    subpage_types = [
        'accounts.UserProfileIndexPage'
    ]

    def create_user_profile_index_page(self):
        if not self.get_children().type(UserProfileIndexPage).exists():
            with transaction.atomic():
                user_profile_index_page = UserProfileIndexPage(
                    title="Users",
                    heading="Welcome to User Profiles",
                    intro="This is a list of user profiles.",
                    slug="u"
                )
                self.add_child(instance=user_profile_index_page)
                return user_profile_index_page
        else:
            # Return the existing page
            return self.get_children().type(UserProfileIndexPage).first()

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class UserProfileIndexPage(Page):
    heading = models.CharField(
        max_length=255,
        blank=True
    )
    intro = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        FieldPanel('intro'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]

    subpage_types = [
        'accounts.UserProfilePage'
    ]
