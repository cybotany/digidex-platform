import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestNewVisitor:
    def test_can_create_profile(self, browser):
        # Edith has heard about a cool new online app for inventory management.
        # She goes to check out its homepage
        browser.get("http://localhost:8000")

        # She notices the page title and header mention DigiDex
        assert "DigiDex" in browser.title

        # She is invited to signup for an account
        signup_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "navbar_signup_button"))
        )
        signup_link.click()

        # She is taken to the signup page
