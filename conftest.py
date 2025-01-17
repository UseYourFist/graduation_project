import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options_lang = Options()
    options_lang.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options_lang)
    yield browser
    browser.quit()