import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        ValueError("Error")
    browser.maximize_window()
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()

