from base.models.page import BasePage

class CategoryIndexPage(BasePage):
    parent_page_types = ["ecommerce.EcommerceIndexPage"]


class CategoryPage(BasePage):
    parent_page_types = ["categories.CategoryIndexPage"]
