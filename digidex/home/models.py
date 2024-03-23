from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import wagtail
from base.blocks import basics as _blocks
from base import models as _models


class HomePage(_models.BasePage):
    body = wagtail.BaseStreamField(
        [
            ('person', _blocks.BaseStructBlock([
                ('first_name', _blocks.BaseCharBlock()),
                ('surname', _blocks.BaseCharBlock()),
                ('photo', _blocks.BaseImageBlock(required=False)),
                ('biography', _blocks.BaseRichTextBlock()),
            ])),
            ('heading', _blocks.BaseCharBlock(form_classname="title")),
            ('paragraph', _blocks.BaseRichTextBlock()),
            ('image', _blocks.BaseImageBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
