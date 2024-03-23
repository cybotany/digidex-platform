from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail
from base.blocks.apps import home as hero
from base.blocks.apps.solutions import section as solutions
from base.models import basics as _models


class HomePage(_models.BasePage):
    hero = wagtail.BaseStreamField(
        [
            ('hero', hero.HeroSectionBlock())
        ],
        null=True,
        blank=True
    )
    solutions = wagtail.BaseStreamField(
        [
            ('solutions', solutions.SolutionSectionBlock())
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero'),
        FieldPanel('solutions'),
    ]
