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


    @pytest.mark.usefixtures("website_url", "browser")
    class TestCataloging:
        def test_correct_title_displayed(self, website_url, browser):
            '''
            The user notices the page title and a header welcoming them
            to the CyBotany platform.
            '''
            browser.get(website_url)
            page_title = browser.title
            assert 'CyBotany' in page_title


    @pytest.mark.django_db
    class TestSignup:
        def test_signup_redirects_to_dashboard(self, client):
            response = client.post(reverse('signup'), {
                'username': 'testuser',
                'password1': 'testpassword',
                'password2': 'testpassword',
            })
            assert response.status_code == 302
            assert response.url == reverse('dashboard')


    @pytest.mark.usefixtures("website_url", "browser")
    class TestLogin:
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