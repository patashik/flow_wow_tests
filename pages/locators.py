from selenium.webdriver.common.by import By

class BasePageLocators():
    COOKIE_FORM = (By.XPATH, '/html/body/noindex/div')
    OK_COOKIE_BUTTON = (By.XPATH, '/html/body/noindex/div/div/div/div[2]/div')
    SEARCH_STRING = (By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/input')
    SWITCH_TO_SHOPS = (By.XPATH, '//*[@id="js-switcher-shops"]')

class MainPageLocators():
    PRODUCTS_POPUPS = (By.XPATH, '//*[@id="js-catalog-products"]/div[1]')

class ResultPageLocators():
    FIRST_SUGGESTION = (By.XPATH, '//*[@id="js-catalog-products"]/div[1]/div/div')
    PRODUCTS_POPUPS = (By.XPATH, '//*[@id="js-catalog-products"]/div[2]')
    SHOPS_POPUPS = (By.XPATH, '//*[@id="js-catalog-shops"]/div[1]')
    SIDEBAR_NAME = (By.XPATH, '//*[@id="js-category-name"]')
    
