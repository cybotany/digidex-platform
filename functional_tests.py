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
def ff_driver():
    return webdriver.Firefox()

WEBSITE_URL = config("WEBSITE_URL")


def test_ff_user_story(ff_driver):
    #User purchased a GL-NFC tag and scans it.
    #After scanning they are prompted to open the web app
    ff_user = TestUser(ff_driver)
    ff_user.browser_navigation(WEBSITE_URL)
        
    # The user notices the page title and header mention cataloging
    # their plant.
    page_title = ff_user.browser.title
    assert 'Plant Catalog' in page_title

    page_header = ff_user.browser.find_element(By.TAG_NAME, 'h1').text
    assert 'Plant Catalog' in page_header

    # They're invited to enter a plant
    inputbox = ff_user.browser.find_element(By.ID, 'id_new_plant')   
    assert inputbox.get_attribute('placeholder') == 'Enter a plant'

    # They type Scindapsus pictus into a text box and hit enter
    inputbox.send_keys('Scindapsus pictus')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(5)
    
    # The page updates and now lists:
    # 1: Scindapsus pictus     
    table = ff_user.browser.find_element(By.ID, 'id_plant_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')  
    assert '1: Scindapsus pictus' in [row.text for row in rows]

    # There is still a text box prompting the user to enter another plant
    inputbox = ff_user.browser.find_element(By.ID, 'id_new_plant')

    # They type Philodendron micans and hit enter.  
    inputbox.send_keys('Philodendron micans')
    inputbox.send_keys(Keys.ENTER)  
    time.sleep(5)  

    # The page updates again, and now shows both items on their list
    table = ff_user.browser.find_element(By.ID, 'id_plant_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')  
    assert '8: Philodendron micans' in [row.text for row in rows]

    # User wonders whether the site will remember their list. Then they sees
    # that the site has generated a unique URL for them -- there is some
    # explanatory text to that effect.

    # They visits that URL - their plant catalog is still there.

    # Satisfied, the user closes the app
    ff_user.quit_browser()