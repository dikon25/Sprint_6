from selenium import webdriver
from config import Url
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.url_main)
    yield driver
    driver.quit()