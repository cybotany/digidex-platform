from base.models.page import BasePage

class ProductIndexPage(BasePage):
    parent_page_types = ["ecommerce.EcommerceIndexPage"]


class ProductPage(BasePage):
    parent_page_types = ["products.ProductIndexPage"]

