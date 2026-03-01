import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_visible_text_without_wait_selenium(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php')

    driver.find_element(By.ID, 'colorChange').click()

    visible_after = driver.find_element(By.ID, 'visibleAfter')

    assert "Visible After 5 Seconds" in visible_after.text


def test_visible_after_text_with_wait(driver):
    driver.get('https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php')

    driver.find_element(By.ID, 'colorChange').click()

    visible_after = WebDriverWait(driver, 6).until(
        EC.visibility_of_element_located((By.ID, 'visibleAfter'))
    )
    assert "Visible After 5 Seconds" in visible_after.text


def test_visible_after_5_seconds_text_selene():
    browser.config.timeout = 10
    browser.open('https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php')

    browser.element('#colorChange').click()

    browser.element('#visibleAfter').should(
        have.text('Visible').and_(have.text('After 5 Seconds'))
    )