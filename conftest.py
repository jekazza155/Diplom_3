import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    global browser
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()

    browser.get(Urls.BASE_URL)
    yield browser
    browser.quit()