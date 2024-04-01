from base.models.body import BasePage

class ProductIndexPage(BasePage):
    parent_page_types = ["ecommerce.EcommerceIndexPage"]


class ProductPage(BasePage):
    parent_page_types = ["products.ProductIndexPage"]

