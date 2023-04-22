import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
        assert error_message is not None
