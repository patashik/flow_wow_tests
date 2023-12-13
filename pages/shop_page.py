from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ShopPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class ShopPage(BasePage):
    def log_in(self):
        login_form = self.is_visible(*ShopPageLocators.LOGIN_FORM)
        assert login_form, 'Can not make order'

    def go_to_make_order(self):
        button = self.is_clickable(*ShopPageLocators.MAKE_ORDER_BUTTON)
        button.click()
        
    def should_be_cart(self, product_name):
        cart = self.is_visible(*ShopPageLocators.CART_FORM)
        product = self.is_visible(*ShopPageLocators.PRODUCT_NAME)
        assert product.text == product_name, 'Product not correct'
    
    