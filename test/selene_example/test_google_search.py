import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search_selenium(driver):
    driver.get("https://www.google.com/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selene github")
    search_box.send_keys(Keys.ENTER)

    expected_text = "yashaka/selene: User-oriented Web UI browser tests in Python"

    h3_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    assert expected_text == h3_element.text

def test_google_search_selene():
    # browser.config.driver.name = "firefox"
    browser.open("https://www.google.com/")

    browser.element("[name=q]").type("selene github").press_enter()

    browser.element("h3").should(have.text("yashaka/selene: User-oriented Web UI browser tests in Python"))
