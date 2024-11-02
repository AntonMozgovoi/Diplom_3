import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.get(Urls.MAIN_PAGE)
    chrome.maximize_window()
    yield chrome
    chrome.quit()



