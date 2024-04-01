from base.models.body import BasePage

class AccountIndexPage(BasePage):
    pass


class LoginPage(BasePage):
    parent_page_types = ["accounts.AccountIndexPage"]
    pass


class SignupPage(BasePage):
    parent_page_types = ["accounts.AccountIndexPage"]
    pass
