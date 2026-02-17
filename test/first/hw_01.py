import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    opts = Options()
    # opts.add_argument("--headless=new") # headless режим браузера - в фоновом режиме, без интерфейса
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


def test_selenium_web(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_selenium_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url
