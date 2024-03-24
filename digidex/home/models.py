from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base.fields import basics as _fields
from base.blocks.apps import (
    home as _hero,
    solution as _solution,
    company as _company,
    support as _support,
)
from base.blocks.components import (
    feature_section as _feature,
    cta_section as _cta,
    faq_section as _faq,
)
from base import models as _models


class HomePage(_models.BasePage):
    body = _fields.BaseStreamField(
        [
            ('hero', _hero.HeroSection()),
            ('solutions', _solution.SolutionSection()),
            ('company', _company.CompanySection()),
            ('features', _feature.FeatureSection()),
            ('reviews', _company.CompanySection()),
            ('support', _support.SupportSection()),
            ('faq', _faq.FAQSection()),
            ('cta', _cta.CallToActionSection()),
        ],
        default=[],
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
