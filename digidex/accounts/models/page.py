from wagtail import models as wt_models

class AccountIndexPage(wt_models.Page):
    parent_page_types = ["home.HomePage"]


class LoginPage(wt_models.Page):
    parent_page_types = ["accounts.AccountIndexPage"]


class SignupPage(wt_models.Page):
    parent_page_types = ["accounts.AccountIndexPage"]
