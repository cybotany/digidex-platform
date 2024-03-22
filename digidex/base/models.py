from wagtail.models import Page
from wagtail.admin.panels import StreamFieldPanel

from base.fields import wagtail_fields as _wfields
from base.blocks import basic_blocks as _bblocks

# Base index page model
class IndexPage(Page):
    introduction = _wfields.BaseStreamField([
        ('paragraph', _bblocks.BaseRichTextBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('introduction'),
    ]

    class Meta:
        abstract = True

class AuthenticationIndexPage(IndexPage):
    pass

class AuthorizationIndexPage(IndexPage):
    pass

class CompanyIndexPage(IndexPage):
    pass

class EcommerceIndexPage(IndexPage):
    pass

class PersonaIndexPage(IndexPage):
    pass

class PrivacyIndexPage(IndexPage):
    pass

class SolutionIndexPage(IndexPage):
    pass

class SupportIndexPage(IndexPage):
    pass
