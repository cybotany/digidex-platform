from base import models as _models


class SolutionsIndexPage(_models.BasePage):
    parent_page_types = ["home.HomePage"]

    class Meta:
        verbose_name = "Solutions Index Page"
        verbose_name_plural = "Solutions Index Pages"
