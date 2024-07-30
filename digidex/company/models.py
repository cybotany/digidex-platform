from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel


class CompanyPage(Page):
    parent_page_types = ["home.HomePage"]
