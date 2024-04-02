from django.db import models
from wagtail import models as wt_models

class EcommerceIndexPage(wt_models.Page):
    heading = models.CharField(max_length=255, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)

class EcommercePage(wt_models.Page):
    heading = models.CharField(max_length=255, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
