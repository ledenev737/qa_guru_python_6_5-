import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'http://demoqa.com'
    browser.config.window_width = 768
    browser.config.window_height = 1360

    yield

    browser.quit()
