from selene import browser


def test_browser_config():
    browser.config.driver_name = 'firefox'

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    browser.config.base_url = 'https://todomvc.com/'