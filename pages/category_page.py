from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import CategoryPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class CategoryPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.is_clickable(*CategoryPageLocators.ADD_TO_CART_BUTTON, 60)
        add_to_cart_button.click()

    def get_page_title(self):
        page_title = self.is_visible(*CategoryPageLocators.PAGE_TITLE)
        return page_title.text
    
    def get_product_card_title(self):
        product_card_title = self.is_visible(*CategoryPageLocators.PRODUCT_CARD_TITLE)
        return product_card_title.text

    def select_product(self):
        product = self.is_clickable(*CategoryPageLocators.PRODUCT_FIRST)
        product_link = self.is_visible(*CategoryPageLocators.PRODUCT_FIRST_LINK)
        product_link = product_link.get_attribute("href")
        product_name = self.is_visible(*CategoryPageLocators.PRODUCT_FIRST_NAME)
        product_name = product_name.text
        product.click()
        self.url_changed()
        assert self.url_contains(product_link), "Did not open product card"
        assert self.get_product_card_title() == product_name, "Product card title incorrect" 
        return product_name

    def switch_to_subcategory(self):
        subcategory_button = self.is_clickable(*CategoryPageLocators.SUBCATEGORY_MONOBOUQETS)
        subcategory_info = self.is_visible(*CategoryPageLocators.SUBCATEGORY_MONOBOUQETS_LINK)
        subcategory_link = subcategory_info.get_attribute("href")
        subcategory_title = subcategory_info.text
        subcategory_button.click()
        self.url_changed()
        assert self.url_contains(subcategory_link), "Did not switch to subcategory"
        assert self.get_page_title() == f'{subcategory_title} в Казани', "Page title incorrect" 