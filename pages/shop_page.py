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
    def go_to_main_page_from_shop_page(self):
        button = self.is_clickable(*ShopPageLocators.LOGO_BUTTON)
        button.click()

    def go_to_make_order(self):
        button = self.is_clickable(*ShopPageLocators.MAKE_ORDER_BUTTON)
        button.click()
        
    def should_be_cart(self):
        assert self.is_visible(*ShopPageLocators.CART_FORM), 'No cart'

    def should_be_product_in_cart(self, product_name):
        product = self.is_visible(*ShopPageLocators.PRODUCT_NAME)
        assert product, 'No product in cart'
        assert product.text == product_name, 'Product in cart not correct'
    
    def should_open_login_form(self):
        assert self.is_visible(*ShopPageLocators.LOGIN_FORM), 'Did not open login form'