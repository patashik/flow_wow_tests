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
        self.has_disappeared(*CategoryPageLocators.PRODUCT_DETAILS_CONTENT)
        self.is_clickable(*CategoryPageLocators.ADD_TO_CART_BUTTON).click()
    
    def click_product(self):
        self.is_clickable(*CategoryPageLocators.PRODUCT_FIRST).click()

    def click_subcategory(self):
        self.is_clickable(*CategoryPageLocators.SUBCATEGORY_BOXES_BUTTON).click()

    def get_page_topic(self):
        page_title = self.is_visible(*CategoryPageLocators.PAGE_TITLE)
        return page_title.text
    
    def get_product_card_title(self):
        product_card_title = self.is_visible(*CategoryPageLocators.PRODUCT_CARD_TITLE)
        return product_card_title.text
   
    def get_product_link(self):
        product_link = self.is_visible(*CategoryPageLocators.PRODUCT_FIRST_LINK)
        product_link = product_link.get_attribute("href")
        return product_link

    def get_product_name(self):
        product_name = self.is_visible(*CategoryPageLocators.PRODUCT_FIRST_NAME)
        product_name = product_name.text
        return product_name
    
    def select_product(self):            
        product_name = self.get_product_name()
        product_link = self.get_product_link()
        self.click_product()
        self.should_change_url()
        self.should_be_correct_url(product_link)
        self.should_be_correct_card_title(product_name)
    
    def should_be_address_tooltip(self):
        self.is_visible(*CategoryPageLocators.ADDRESS_TOOLTIP)
    
    def should_be_correct_page_topic(self, subcategory_title):
        assert self.get_page_topic() == f'{subcategory_title} в Казани', "Page title incorrect" 

    def should_be_correct_card_title(self, product_name):
        assert self.get_product_card_title() == product_name, "Product card title incorrect" 

    def get_subcategory_title(self):
        subcategory_info = self.is_visible(*CategoryPageLocators.SUBCATEGORY_BOXES_LINK)
        subcategory_title = subcategory_info.text
        return subcategory_title 
    
    def get_subcategory_link(self):
        subcategory_info = self.is_visible(*CategoryPageLocators.SUBCATEGORY_BOXES_LINK)
        subcategory_link = subcategory_info.get_attribute("href")
        return subcategory_link 

    def switch_to_subcategory(self):
        subcategory_link = self.get_subcategory_link()
        subcategory_title = self.get_subcategory_title()
        self.click_subcategory()
        self.should_change_url()
        self.should_be_correct_url(subcategory_link)
        self.should_be_correct_page_topic(subcategory_title)