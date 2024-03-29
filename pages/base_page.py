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
            assert status_code == code, "HTTP status code not correct"
        except TimeoutException:
            return False
        return True

    def accept_cookies(self):
        self.is_clickable(*BasePageLocators.OK_COOKIE_BUTTON).click()
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

    def attribute_text_is(self, locator, attribute, text):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.text_to_be_present_in_element_attribute(locator, attribute, f'{text}'))
        except TimeoutException:
            return False
        return True

    def click_set_address(self):
        self.is_clickable(*BasePageLocators.ADDRESS_BUTTON).click()
    
    def click_time_settings(self):
        self.is_clickable(*BasePageLocators.TIME_BUTTON).click()

    def element_text_is(self, how, what, text, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.text_to_be_present_in_element((how, what), f'{text}'))
        except TimeoutException:
            return False
        return True
    
    def fill_short_address_form(self, address):
        self.insert_address(address)
        self.select_address_from_list(address)
        self.is_clickable(*BasePageLocators.ADDRESS_ACCEPT_BUTTON).click()
    
    def fill_detailed_address_form(self, house, office, comment):
        house_form = self.is_clickable(*BasePageLocators.ADDRESS_HOUSE)
        house_form.click()
        house_form.send_keys(house)
        office_form = self.is_clickable(*BasePageLocators.ADDRESS_OFFICE)
        office_form.click()
        office_form.send_keys(office)
        comment_form = self.is_clickable(*BasePageLocators.ADDRESS_COMMENT)
        comment_form.click()
        comment_form.send_keys(comment)    
        accept_button = self.is_clickable(*BasePageLocators.ADDRESS_ACCEPT_BUTTON_DETAILED)
        accept_button.click()
          
    def go_to_category_page(self):
        self.is_clickable(*BasePageLocators.CATEGORY_FLOWERS).click()

    def go_to_main_page(self):
        self.is_clickable(*BasePageLocators.LOGO_BUTTON).click()

    def has_disappeared(self, how, what, timeout=40):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_clickable(self, how, what, timeout=30):
        try:
            element = WebDriverWait(self.browser, timeout, 2).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return element

    def is_visible(self, how, what, timeout=100):
        try:
            element = WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return element
    
    def insert_address(self, address):
        address_input = self.is_clickable(*BasePageLocators.ADDRESS_INPUT)
        address_input.click()
        address_input.send_keys(address)
       
    def insert_search_request(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        symbols = list(search_request)
        for i in symbols:
            search_string.click()
            search_string.send_keys(i)

    def maximize_window(self):
        self.browser.maximize_window()
    
    def resize_window(self, width, height):
        self.browser.set_window_size(width, height)

    def save_selected_time(self):
        self.has_disappeared(*BasePageLocators.TIME_WHEN_LIST)
        self.is_clickable(*BasePageLocators.TIME_SAVE_BUTTON).click()

    def select_address_from_list(self, address):
        self.is_visible(*BasePageLocators.ADDRESS_LIST)
        assert self.element_text_is(*BasePageLocators.ADDRESS_FIRST_ITEM, address)
        address_item = self.is_clickable(*BasePageLocators.ADDRESS_FIRST_ITEM)
        address_item.click()
        
    def select_day(self):
        self.is_clickable(*BasePageLocators.TIME_TOMORROW).click()
        return self.is_visible(*BasePageLocators.TIME_TOMORROW_TEXT).text
    
    def select_popular_request(self):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        search_string.click()
        popular_request_first = self.is_clickable(*BasePageLocators.POPULAR_REQUESTS_FIRST)
        return popular_request_first

    def select_recommendation(self):
        recommendation = self.is_clickable(*BasePageLocators.RECOMMENDATION_SECOND)
        return recommendation

    def select_time_asap(self):
        self.is_clickable(*BasePageLocators.TIME_ITEM_ASAP).click()

    def select_time_detailed(self):
        self.is_clickable(*BasePageLocators.TIME_ITEM_DETAILED).click()

    def select_time_period(self):
        self.is_clickable(*BasePageLocators.TIME_WHEN_LIST).click()
        self.is_clickable(*BasePageLocators.TIME_WHEN_ITEM).click()
        return self.is_clickable(*BasePageLocators.TIME_WHEN_ITEM).text

    def select_time_receiver(self):
        self.is_clickable(*BasePageLocators.TIME_ITEM_RECEIVER).click()

    def select_shop_recommendation(self):
        shop_recommendation = self.is_clickable(*BasePageLocators.RECOMMENDATION_SHOP)
        return shop_recommendation

    def should_be_content_in_url(self, content):
        assert self.url_contains(content), 'Page url incorrect'

    def should_be_correct_url(self, new_url):
        assert self.url_to_be(new_url), 'Page url incorrect'

    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.is_visible(*BasePageLocators.SEARCH_STRING)
        assert search_string.get_attribute("value") == search_request, 'No search request in search string'

    def should_be_search_request_in_url(self, search_request):
        assert self.url_contains(f'query={quote(search_request)}'), 'Search did not start'
    
    def should_be_setted_address(self, address, house):
        setted_address = self.is_visible(*BasePageLocators.ADDRESS_BUTTON)
        assert setted_address.text == f'Казань, {address}, {house}', 'Setted address incorrect'
        
    def should_be_setted_time_asap(self):
        setted_time = self.is_visible(*BasePageLocators.TIME_BUTTON)
        assert setted_time.text == f'Как можно скорее', 'Time settings incorrect'

    def should_be_setted_time_detailed(self, day, time):
        setted_time = self.is_visible(*BasePageLocators.TIME_BUTTON)
        assert setted_time.text == f'{day}, {time}', 'Time settings incorrect'

    def should_be_setted_time_receiver(self, day):
        setted_time = self.is_visible(*BasePageLocators.TIME_BUTTON)
        assert setted_time.text == f'{day}, время согласуем', 'Time settings incorrect'

    def should_be_page_title(self, page_title):
        assert self.title_is(page_title), 'Page title incorrect'

    def should_change_url(self):
        assert self.url_changes(), "Url did not change"
    
    def should_disappear_address_form(self):
        assert self.has_disappeared(*BasePageLocators.ADDRESS_FORM), 'Address not accepted'

    def should_disappear_detailed_address_form(self):
        assert self.has_disappeared(*BasePageLocators.ADDRESS_FORM_DETAILED), 'Address not accepted'

    def should_open_address_form(self):
        assert self.is_clickable(*BasePageLocators.ADDRESS_FORM), 'Did not open address form'

    def should_open_category_page(self):
        category_page_url = "https://flowwow.com/kazan/"
        assert self.url_to_be(category_page_url), 'Did not open category page'

    def should_open_main_page(self):
        main_page_url = "https://flowwow.com/kazan/all-products/" 
        assert self.url_to_be(main_page_url), 'Did not open main page'

    def should_open_shop_page(self):
        shop_page_url = "https://flowwow.com/shop/"
        assert self.url_contains(shop_page_url), 'Did not open shop page'

    def should_open_start_page(self):
        start_page_url = "https://flowwow.com/"
        assert self.url_contains(start_page_url), 'Did not open start page'

    def should_open_time_form(self):
        assert self.is_clickable(*BasePageLocators.TIME_FORM), 'Did not open time form'

    def should_switch_to_shops(self):
        self.is_visible(*BasePageLocators.SWITCH_TO_SHOPS).click()

    def start_search_by_request(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        symbols = list(search_request)
        for i in symbols:
            search_string.click()
            search_string.send_keys(i)

        search_string.click()
        search_string.send_keys(Keys.ENTER)
      
    def switch_to_shop_window(self):
        shop_window = self.browser.window_handles[1]
        self.browser.switch_to.window(shop_window)

    def title_is(self, page_title, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.title_is((page_title)))
        except TimeoutException:
            return False
        return True

    def url_changes(self, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_changes((self.url)))
        except TimeoutException:
            return False
        return True
    
    def url_contains(self, url_text, timeout=60):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_contains(url_text))
        except TimeoutException:
            return False
        return True
        
    def url_to_be(self, new_url, timeout=60):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_to_be(new_url))
        except TimeoutException:
            return False
        return True