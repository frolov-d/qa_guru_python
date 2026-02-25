import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def headless_chrome():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_page_title_selenium(headless_chrome):
    headless_chrome.get("https://example.com")

    assert headless_chrome.title == "Example domain"


def test_page_title_selene():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    browser.config.driver_options = options

    browser.open("https://example.com")

    browser.should(have.title("Example Domain"))

