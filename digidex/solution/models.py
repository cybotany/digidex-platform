from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from base import models as base_models

class SolutionIndexPage(base_models.IndexPage):
    pass

class SolutionsPage(Page):
    pass