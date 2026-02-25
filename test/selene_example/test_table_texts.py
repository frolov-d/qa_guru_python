import pytest
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_table_texts_selenium(driver):
    driver.get(
        'https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')

    table = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'customers'))
    )

    tr_elements = table.find_elements(By.TAG_NAME, 'tr')

    expected_texts = ['Company Contact Country', 'Google Maria Anders Germany',
                      'Meta Francisco Chang Mexico',
                      'Microsoft Roland Mendel Austria',
                      'Island Trading Helen Bennett UK',
                      'Adobe Yoshi Tannamuri Canada',
                      'Amazon Giovanni Rovelli Italy', ]
    actual_texts = [element.text for element in tr_elements]
    assert actual_texts == expected_texts


def test_table_texts_selene():
    browser.open(
        'https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html'
    )

    browser.element('#customers').all('tr').should(
        have.exact_texts(
            'Company Contact Country',
            'Google Maria Anders Germany',
            'Meta Francisco Chang Mexico',
            'Microsoft Roland Mendel Austria',
            'Island Trading Helen Bennett UK',
            'Adobe Yoshi Tannamuri Canada',
            'Amazon Giovanni Rovelli Italy',
        )
    )