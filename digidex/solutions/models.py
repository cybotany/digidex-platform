from wagtail import models as wt_models


class SolutionsIndexPage(wt_models.Page):
    parent_page_types = ["home.HomePage"]

    class Meta:
        verbose_name = "Solutions Index Page"
        verbose_name_plural = "Solutions Index Pages"
