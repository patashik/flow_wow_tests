from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import urllib.parse
from urllib.parse import quote

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_correct_response_status_code(self):
        code = 200
        try:
            status_code = requests.get(self.browser.current_url).status_code
            print(self.browser.current_url)
            print(status_code)
            assert status_code == code, "Status not correct"
        except TimeoutException:
            return False
        return True

    def accept_cookies(self):
        ok_cookie_button = self.is_clickable(*BasePageLocators.OK_COOKIE_BUTTON)
        ok_cookie_button.click()
        self.has_disappeared(*BasePageLocators.COOKIE_FORM)
    
    def any_of(self, how1, what1, how2, what2, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.any_of(
                    EC.presence_of_element_located((how1, what1)),
                    EC.presence_of_element_located((how2, what2)),
                )
            )
        except TimeoutException:
            return False
        return True

    def has_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_clickable(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.element_to_be_clickable((how, what)))
        return element

    def is_presented(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.presence_of_element_located((how, what)))
        return element
    
    def is_visible(self, how, what, timeout=100):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
        return element

    def insert_search_request(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        symbols = list(search_request)
        for i in symbols:
            search_string.click()
            search_string.send_keys(i)
    
    def select_popular_request(self):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        search_string.click()
        popular_requests_list = self.is_visible(*BasePageLocators.POPULAR_REQUESTS_LIST)
        popular_request_first = self.is_clickable(*BasePageLocators.POPULAR_REQUESTS_FIRST)
        return popular_request_first

    def select_recommendation(self):
        recommendation = self.is_clickable(*BasePageLocators.RECOMMENDATION_SECOND)
        return recommendation

    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.is_visible(*BasePageLocators.SEARCH_STRING)
        assert search_string.get_attribute("value") == search_request, 'No search request in search string'

    def should_be_search_request_in_url(self, search_request):
        assert self.url_contains(f'query={quote(search_request)}'), 'Search did not start'
    
    def should_switch_to_shops(self):
        switch_to_shops = self.is_visible(*BasePageLocators.SWITCH_TO_SHOPS)
        switch_to_shops.click()
        self.url_changed()
        assert self.url_contains("all-shops"), 'Did not switch to shops'

    def start_search_by_popular_request(self, popular_request, popular_request_text):
        popular_request.click()
        self.url_changed()
        self.should_be_search_request_in_url(popular_request_text)
    
    def start_search_by_request(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        symbols = list(search_request)
        for i in symbols:
            search_string.click()
            search_string.send_keys(i)
        search_string.click()
        search_string.send_keys(Keys.ENTER)
        self.url_changed()
        self.should_be_search_request_in_url(search_request)
    
    def start_search_by_text_and_recommendation(self, recommendation, recommendation_text):
        recommendation.click()
        self.url_changed()
        self.should_be_search_request_in_url(recommendation_text)
    
    def url_changed(self, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_changes((self.browser.current_url)))
        except TimeoutException:
            return False
        return True

    def url_contains(self, url_text, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_contains(url_text))
        except TimeoutException:
            return False
        return True
        
    def url_to_be(self, new_url, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_to_be(new_url))
        except TimeoutException:
            return False
        return True