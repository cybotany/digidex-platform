from wagtail.models import Page


class BasePage(Page):
    pass

    class Meta:
        abstract = True


class BaseIndexPage(BasePage):
    pass

    class Meta:
        abstract = True
