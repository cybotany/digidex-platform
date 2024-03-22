from wagtail.core.models import Page
from wagtail.admin.panels import StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock

# Base index page model
class IndexPage(Page):
    introduction = StreamField([
        ('paragraph', RichTextBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('introduction'),
    ]

    class Meta:
        abstract = True

# For the Authentication app
class AuthenticationIndexPage(IndexPage):
    pass  # You can customize this class as needed.

# For the Authorization app
class AuthorizationIndexPage(IndexPage):
    pass

# For the Company app
class CompanyIndexPage(IndexPage):
    pass

# For the Ecommerce app
class EcommerceIndexPage(IndexPage):
    pass

# For the Persona app
class PersonaIndexPage(IndexPage):
    pass

# For the Privacy app
class PrivacyIndexPage(IndexPage):
    pass

# For the Solution app
class SolutionIndexPage(IndexPage):
    pass

# For the Support app
class SupportIndexPage(IndexPage):
    pass
