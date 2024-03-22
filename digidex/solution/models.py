from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail_fields as _wfields
from base.blocks import basic_blocks as _bblocks
from digidex.base import models as base_models
from solution import blocks as _sblocks

class SolutionIndexPage(base_models.IndexPage):
    pass

class SolutionsPage(Page):
    top_section = _wfields.BaseStreamField(
        [
            ('heading', _bblocks.BaseCharBlock(form_classname="full title")),
            ('paragraph', _bblocks.BaseRichTextBlock()),
        ],
        null=True,
        blank=True
    )
    about_sections = _wfields.BaseStreamField(
        [
            ('about_section', _sblocks.AboutSectionBlock()),
        ],
        null=True,
        blank=True
    )
    quote = _wfields.BaseStreamField(
        [
            ('quote', _sblocks.QuoteBlock()),
        ],
        null=True,
        blank=True
    )
    team_members = _wfields.BaseStreamField(
        [
            ('team_member', _sblocks.TeamMemberBlock()),
        ],
        null=True,
        blank=True
    )
    reviews = _wfields.BaseStreamField(
        [
            ('review', _sblocks.ReviewBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('top_section'),
        FieldPanel('about_sections'),
        FieldPanel('quote'),
        FieldPanel('team_members'),
        FieldPanel('reviews'),
    ]
