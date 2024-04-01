from base.models.body import BasePage

class AccountIndexPage(BasePage):
    parent_page_types = ["home.HomePage"]


class LoginPage(BasePage):
    parent_page_types = ["accounts.AccountIndexPage"]


class SignupPage(BasePage):
    parent_page_types = ["accounts.AccountIndexPage"]
