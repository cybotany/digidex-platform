from wagtail import models as wt_models

class CategoryIndexPage(wt_models.Page):
    parent_page_types = ["ecommerce.EcommerceIndexPage"]


class CategoryPage(wt_models.Page):
    parent_page_types = ["categories.CategoryIndexPage"]
