import time
from decouple import config
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


WEBSITE_URL = config("WEBSITE_URL")

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
    def test_correct_header_and_title_displayed(self, url):
        '''
        The user notices the page title and header
        mention cataloging their plant.
        '''
        self.browser_navigation(url)
        page_title = self.browser.title
        assert 'Plant Catalog' in page_title

        page_header = self.browser.find_element(By.TAG_NAME, 'h1').text
        assert 'Plant Catalog' in page_header


    def test_prompt_to_enter_plant(self):
        # They're invited to enter a plant
        inputbox = self.browser.find_element(By.ID, 'id_new_plant')   
        assert inputbox.get_attribute('placeholder') == 'Enter a plant'


    def test_plant_entered_and_listed(self):
        # They type Scindapsus pictus into a text box and hit enter
        inputbox = self.browser.find_element(By.ID, 'id_new_plant')   
        assert inputbox.get_attribute('placeholder') == 'Enter a plant'
        inputbox.send_keys('Scindapsus pictus')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
    
        # The page updates and now lists:
        # 1: Scindapsus pictus     
        table = self.browser.find_element(By.ID, 'id_plant_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')  
        assert '1: Scindapsus pictus' in [row.text for row in rows]


    def test_plant_entered_and_listed(self):
        # There is still a text box prompting the user to enter another plant
        inputbox = ff_user.browser.find_element(By.ID, 'id_new_plant')

        # They type Philodendron micans and hit enter.  
        inputbox.send_keys('Philodendron micans')
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(5)  

        # The page updates again, and now shows both items on their list
        table = ff_user.browser.find_element(By.ID, 'id_plant_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')  
        assert '2: Philodendron micans' in [row.text for row in rows]

    # User wonders whether the site will remember their list. Then they sees
    # that the site has generated a unique URL for them -- there is some
    # explanatory text to that effect.

    # They visits that URL - their plant catalog is still there.

    # Satisfied, the user closes the app
    def clean_up(self):
        self.quit_browser()