from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from base.blocks import basic_blocks as _bblocks
from solution import blocks as _sblocks

class SolutionsPage(Page):
    top_section = StreamField([
        ('heading', _bblocks.BaseCharBlock(form_classname="full title")),
        ('paragraph', _bblocks.BaseRichTextBlock()),
    ], null=True, blank=True)

    about_sections = StreamField([
        ('about_section', _sblocks.AboutSectionBlock()),
    ], null=True, blank=True)

    quote = StreamField([
        ('quote', _sblocks.QuoteBlock()),
    ], null=True, blank=True)

    team_members = StreamField([
        ('team_member', _sblocks.TeamMemberBlock()),
    ], null=True, blank=True)

    reviews = StreamField([
        ('review', _sblocks.ReviewBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('top_section'),
        StreamFieldPanel('about_sections'),
        StreamFieldPanel('quote'),
        StreamFieldPanel('team_members'),
        StreamFieldPanel('reviews'),
    ]
