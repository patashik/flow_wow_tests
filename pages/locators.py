from selenium.webdriver.common.by import By

class BasePageLocators():
    COOKIE_FORM = (By.XPATH, '/html/body/noindex/div')
    OK_COOKIE_BUTTON = (By.XPATH, '/html/body/noindex/div/div/div/div[2]/div')
    SEARCH_STRING = (By.XPATH, '/html/body/div[2]/div/div[4]/div[1]/input')
    SUGGESTIONS_LIST = (By.XPATH, '//*[@id="js-search-suggestions"]')
    SUGGESTION_ITEM = (By.XPATH, '//*[@id="js-search-suggestions"]/div[1]')
    SWITCH_TO_SHOPS = (By.XPATH, '//*[@id="js-switcher-shops"]')
    
class MainPageLocators():
    PRODUCTS_POPUPS = (By.XPATH, '//*[@id="js-catalog-products"]/div[1]')

class ResultPageLocators():
    RECOMMENDATION_FIRST = (By.XPATH, '//*[@id="js-catalog-products"]/div[1]/div/div')
    RECOMMENDATION_SECOND = (By.XPATH, '//*[@id="js-catalog-products"]/div[1]/div/div[2]')
    PRODUCTS_POPUPS = (By.XPATH, '//*[@id="js-catalog-products"]/div[2]')
    SHOPS_POPUPS = (By.XPATH, '//*[@id="js-catalog-shops"]/div[1]')
    SIDEBAR_NAME = (By.XPATH, '//*[@id="js-category-name"]')