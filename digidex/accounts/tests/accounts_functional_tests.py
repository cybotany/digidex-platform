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
            EC.presence_of_element_located((By.ID, "signup_link"))
        )
        signup_link.click()

        # She is taken to the signup page
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        # She fills out the form and submits it
        username_field = browser.find_element(By.NAME, "username")
        username_field.send_keys("edith_example")

        password_field = browser.find_element(By.NAME, "password")
        password_field.send_keys("S3cr3t!")

        browser.find_element(By.NAME, "submit").click()

        # She is redirected to a page confirming her registration
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Registration successful"))

        # She notices a link to her profile page and clicks it
        profile_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "profile_link"))
        )
        profile_link.click()

        # She sees her user information displayed
        WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "edith_example's Profile"))

        # Satisfied, she goes back to sleep
