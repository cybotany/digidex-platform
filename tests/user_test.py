import time
from decouple import config
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestUser:
    '''
    Class for testing the web-app experience from the
    point of view of the user.

    User Story:
        User purchases a CyBotany tag and scans it. After
        scanning they are prompted to open the web app using
        the default browser on their phone.
    '''

    @pytest.mark.usefixtures("ff_driver")
    def __init__(self, driver):
        self.browser = driver
    
    def browser_navigation(self, website):
        self.browser.get(website)

    def quit_browser(self):
        self.browser.quit()

    @pytest.mark.usefixtures("website_url")
    def test_correct_title_displayed(self, url):
        '''
        The user notices the page title and header
        mention cataloging their plant.
        '''
        self.browser_navigation(url)
        page_title = self.browser.title
        assert 'CyBotany' in page_title


    def clean_up(self):
        self.quit_browser()