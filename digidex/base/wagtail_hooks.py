from wagtail.snippets.models import register_snippet

from base.models import HeaderAdvertisement, FooterContent, FooterNotice

register_snippet(HeaderAdvertisement)
register_snippet(FooterContent)
register_snippet(FooterNotice)