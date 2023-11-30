import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
    
@pytest.fixture(scope="function")
def browser_chrome():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def browser_firefox():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()
