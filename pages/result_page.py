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
    def should_be_any_result_message(self):
        assert self.any_of(*ResultPageLocators.FOUND_MESSAGE, *ResultPageLocators.NOT_FOUND_MESSAGE), 'Incorrect search'
    
    def should_be_found_message(self):
        assert self.is_visible(*ResultPageLocators.FOUND_MESSAGE), 'Result message is missing'
    
    def should_be_not_found_message(self):
        assert self.is_visible(*ResultPageLocators.NOT_FOUND_MESSAGE), 'Result message is missing'

    def should_be_recommendation_message(self, search_request):
        recommendation_message = self.is_visible(*ResultPageLocators.RECOMMENDATION_MESSAGE)
        assert recommendation_message.text == f'{search_request}', 'Recommendation incorrect'
    
    def should_be_products_popups(self):
        assert self.is_visible(*ResultPageLocators.PRODUCTS_POPUPS), 'No products popups'