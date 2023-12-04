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
        assert self.any_of(*ResultPageLocators.FOUND_MESSAGE, *ResultPageLocators.NOT_FOUND_MESSAGE)
    
    def should_be_found_message(self):
        found_message = self.is_visible(*ResultPageLocators.FOUND_MESSAGE)
        assert found_message, 'Result message is missing'
    
    def should_be_not_found_message(self):
        not_found_message = self.is_visible(*ResultPageLocators.NOT_FOUND_MESSAGE)
        assert not_found_message, 'Result message is missing'

    def should_be_recommendation_message(self, search_request):
        recommendation_message = self.is_visible(*ResultPageLocators.RECOMMENDATION_MESSAGE)
        assert recommendation_message.text == f'{search_request}'
    
    def should_be_products_popups(self):
        products_popups = self.is_visible(*ResultPageLocators.PRODUCTS_POPUPS)
        assert products_popups, 'No products popups'

    def should_be_shops_popups(self):
        shops_popups = self.is_visible(*ResultPageLocators.SHOPS_POPUPS)
        assert shops_popups, 'No shops popups'
    
    def should_be_recommendations(self, search_request):
        first_recommendation = self.is_visible(*ResultPageLocators.RECOMMENDATION_FIRST)
        assert first_recommendation.text == f'{search_request}', 'No recommendations for search'

    def select_single_recommendation(self):
        second_recommendation = self.is_clickable(*ResultPageLocators.RECOMMENDATION_SECOND)
        return second_recommendation

    def should_be_search_request_in_fields(self, search_request):
        self.should_be_search_request_in_url(search_request)
        self.should_be_search_request_in_search_string(search_request)
        self.should_be_sidebar_name(search_request)
        self.should_be_recommendations(search_request)
    
    def search_by_recommendation(self):
        recommendation = self.select_single_recommendation()
        text = recommendation.text
        recommendation.click()
        self.url_changed()
        self.should_be_search_request_in_fields(text)