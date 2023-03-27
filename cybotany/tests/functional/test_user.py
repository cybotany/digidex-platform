from decouple import config
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

@pytest.fixture
def client():
    return Client()

@pytest.mark.usefixtures("website_url", "browser")
class TestUser:
    '''
    Class for testing the web-app experience from the
    point of view of the user.

    User Story:
        User purchases a CyBotany tag and scans it. After
        scanning they are prompted to open the web app using
        the default browser on their phone.
    '''

    @pytest.fixture(scope='class')
    def browser(self, ff_driver):
        browser = ff_driver
        yield browser
        browser.quit()

    def test_correct_title_displayed(self, website_url, browser):
        '''
        The user notices the page title and a header welcoming them
        to the CyBotany platform.
        '''
        browser.get(website_url)
        page_title = browser.title
        assert 'CyBotany' in page_title

    def test_user_can_navigate_to_signup_and_fill_info(self, website_url, browser):
        # User visits the home page
        browser.get(website_url)
        
        # User sees a link to the signup page and clicks it
        signup_link = browser.find_element(By.ID, "signup-link")
        signup_link.click()
        
        # User is redirected to the signup page
        assert browser.current_url == website_url + "signup/"
        
        # User fills in their information and submits the form
        username_input = browser.find_element(By.NAME, "username")
        email_input = browser.find_element(By.NAME, "email")
        password_input = browser.find_element(By.NAME, "password")
        password_confirm_input = browser.find_element(By.NAME, "confirm_password")
        
        username_input.send_keys("new_user")
        email_input.send_keys("new_user@example.com")
        password_input.send_keys("valid_password")
        password_confirm_input.send_keys("valid_password")
        password_confirm_input.send_keys(Keys.RETURN)
        
        # User is redirected to the separate page to fill in their info
        assert browser.current_url == website_url + "signup/info/"


    def test_login_page_displays(self, website_url, browser):
        '''
        The user notices two text boxes for username and password
        on the login page.
        '''
        browser.get(website_url + "login/")
        wait = WebDriverWait(browser, 10)
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        assert username_input is not None
        assert password_input is not None

    def test_login_valid_credentials_redirect_to_dashboard(self, website_url, browser):
        '''
        The user enters valid login credentials and is redirected
        to their dashboard.
        '''
        browser.get(website_url + "login/")
        wait = WebDriverWait(browser, 10)
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        username_input.send_keys(config('TEST_USERNAME'))
        password_input.send_keys(config('TEST_PASSWORD'))
        password_input.send_keys(Keys.RETURN)
        assert browser.current_url == website_url + "dashboard/"

    def test_login_invalid_credentials_displays_error(self, website_url, browser):
        '''
        The user enters invalid login credentials and an error message
        is displayed on the page.
        '''
        browser.get(website_url + "login/")
        wait = WebDriverWait(browser, 10)
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        username_input.send_keys("invalid_username")
        password_input.send_keys("invalid_password")
        password_input.send_keys(Keys.RETURN)
        error_message = browser.find_element(By.CSS_SELECTOR, ".alert-danger")
        assert error_message is not None
