from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from base.models import FooterBanner, FooterParagraph, FooterCopyright


class FooterParagraphViewSet(SnippetViewSet):
    model = FooterParagraph
    icon = "crosshairs"
    menu_label = "Footer Paragraph"
    menu_name = "footer paragraph"

    panels = [
        FieldPanel("paragraph"),
    ]


class FooterCopyrightViewSet(SnippetViewSet):
    model = FooterCopyright
    icon = "desktop"
    menu_label = "Footer Copyright"
    menu_name = "footer copyright"

    panels = [
        FieldPanel("copyright"),
        PublishingPanel(),
    ]


class FooterViewSetGroup(SnippetViewSetGroup):
    items = (FooterParagraphViewSet, FooterCopyrightViewSet)
    menu_icon = "folder-inverse"
    menu_label = "Footer"
    menu_name = "footer"


register_snippet(FooterViewSetGroup)