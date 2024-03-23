from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields
from base.blocks.apps import home as hero_section
from base.blocks.apps.solutions import section as solution_section


class HomePage(Page):
    hero = wagtail_fields.BaseStreamField(
        [
            ('hero', hero_section.HeroSectionBlock())
        ],
        null=True,
        blank=True
    )
    solutions = wagtail_fields.BaseStreamField(
        [
            ('solutions', solution_section.SolutionSectionBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_section'),
        FieldPanel('features'),
    ]
