import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import config


# setup and tear down method
@pytest.fixture()
def setup():
    s = Service(config.Config.chrome_path)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(config.Config.gmail_url)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
