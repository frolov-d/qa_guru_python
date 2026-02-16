import pytest
from selenium import webdriver

@pytest.mark.selenium
def test_selenium():
    driver = webdriver.Chrome()
    url = 'https://www.selenium.dev/'
    driver.get(url)

    assert driver.title == 'Selenium'
    assert driver.current_url == url