from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class ShopPage(BasePage):
    def click(self):
        sidebar_name = self.is_visible(*MainPageLocators.PRODUCTS_POPUPS)
    