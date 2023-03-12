from selenium import webdriver
import pytest
from decouple import config

browser = webdriver.Firefox()
website = config("WEBSITE_URL")

# User purchased a GL-NFC tag and scans it to register
# it. After scanning, a web-app launches.
browser.get(website)

