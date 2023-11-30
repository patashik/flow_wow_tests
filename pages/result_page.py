from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ResultPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class ResultPage(BasePage):
    def should_be_sidebar_name(self, search_request):
        sidebar_name = self.is_visible(*ResultPageLocators.SIDEBAR_NAME)
        assert sidebar_name.text == f'Результаты по запросу «{search_request}»', 'No search request in sidebar'
    
    def should_be_products_popups(self):
        products_popups = self.is_visible(*ResultPageLocators.PRODUCTS_POPUPS)
        assert products_popups, 'No products popups'

    def should_be_shops_popups(self):
        shops_popups = self.is_visible(*ResultPageLocators.SHOPS_POPUPS)
        assert shops_popups, 'No shops popups'
    
    def should_be_suggestions(self, search_request):
        suggestion = self.is_visible(*ResultPageLocators.FIRST_SUGGESTION)
        assert suggestion.text == f'{search_request}', 'No suggestions for search'

    def should_be_search_results_in_menu(self, search_request):
        self.should_be_search_request_in_search_string(search_request)
        self.should_be_sidebar_name(search_request)
