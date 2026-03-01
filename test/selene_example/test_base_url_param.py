import pytest
from selene import browser, have

browser.config.base_url = 'https://todomvc.com'


@pytest.mark.parametrize(
    'relative_url',
    ['/examples/preact/dist', '/examples/vue/dist/#', '/examples/angular/dist/browser/#/all'],
    ids=['preact', 'vue', 'angular']
)
def test_todomvc(relative_url):
    browser.open(relative_url)

    browser.element('.new-todo').type('My first task').press_enter()

    browser.all('.todo-list li').should(have.exact_texts('My first task'))