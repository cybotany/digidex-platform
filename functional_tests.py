from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from decouple import config
import pytest

class TestUser:
    __test__ = False

    def __init__(self, browser):
        self.browser = browser
    
    def browser_navigation(self, website):
        self.browser.get(website)

    def quit_browser(self):
        self.browser.quit()

@pytest.fixture
def firefox_user():
    return webdriver.Firefox()

WEBSITE_URL = config("WEBSITE_URL")

def test_ff_user_story(firefox_user):
    #User purchased a GL-NFC tag and scans it.
    #After scanning they are prompted to open the web app
    ff_user = TestUser(firefox_user)
    ff_user.browser_navigation(WEBSITE_URL)
        
    # The user notices the page title and header mention cataloging
    # their plant.
    page_title = ff_user.browser.title
    assert 'Plant Catalog' in page_title

    page_header = ff_user.browser.find_element(By.TAG_NAME, 'h1').text
    assert 'Plant Catalog' in page_header

    # They're invited to enter a to-do item straight away
    inputbox = ff_user.browser.find_element(By.ID, 'id_new_item')   
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

    # They type "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)
    inputbox.send_keys('Buy peacock feathers')
    
    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list
    inputbox.send_keys(Keys.ENTER)  
    time.sleep(1)  

    table = ff_user.browser.find_element(By.ID, 'id_list_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')  
    assert any(row.text == '1: Buy peacock feathers' for row in rows) is True

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very methodical)

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep
    ff_user.quit_browser()