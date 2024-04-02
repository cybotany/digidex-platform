from wagtail import models as wt_models

class ProductIndexPage(wt_models.Page):
    parent_page_types = ["ecommerce.EcommerceIndexPage"]


class ProductPage(wt_models.Page):
    parent_page_types = ["products.ProductIndexPage"]
