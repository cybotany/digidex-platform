from selenium import webdriver
from decouple import config
import pytest

class TestUser:
    def __init__(self, browser):
        self.browser = browser
    
    def browser_navigation(self, website):
        self.browser.get(website)

    def quit_browser(self):
        self.browser.quit()

@pytest.fixture
def firefox_user():
    return TestUser(webdriver.Firefox())

def main():

    WEBSITE_URL = config("WEBSITE_URL")

    # User purchased a GL-NFC tag and scans it.
    # After scanning they are prompted to open the web app
    def test_page_launch(firefox_user):
        ff_user = TestUser(firefox_user)
        ff_user.browser_navigation(WEBSITE_URL)
        ff_user.quit()

    # The user notices the page title and header mention cataloging
    # their plant.
    #assert 'Plant Catalog' in browser.title

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box (Edith's hobby
    # is tying fly-fishing lures)

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very methodical)

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep

if __name__ == '__main__':
    main()
