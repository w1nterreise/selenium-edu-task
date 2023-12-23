import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox




def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
 
    if browser_name == "chrome":  
        options_chrome = OptionsChrome()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})    
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
        
    yield browser  
    browser.quit()