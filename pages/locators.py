from selenium.webdriver.common.by import By

class BasePageLocators():
    ADDRESS_BUTTON = (By.XPATH, '//*[@id="grid"]/header/div/header/div/div[1]/div/div/div[2]/span[1]')
    ADDRESS_ACCEPT_BUTTON = (By.XPATH, '//*[@id="AddressStreetModal"]/div/div/div/div[4]/button')
    ADDRESS_COMMENT = (By.XPATH, '//*[@id="AddressStreetModal"]/div/div/div/div[3]/div[2]/div[2]/textarea')
    ADDRESS_FIRST_ITEM = (By.XPATH, '//*[@id="AddressModal"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/section/ul/li[1]')
    ADDRESS_FORM = (By.XPATH, '//*[@id="AddressModal"]/div/div')
    ADDRESS_FORM_DETAILED = (By.XPATH, '/*[@id="AddressStreetModal"]/div/div')
    ADDRESS_HOUSE = (By.XPATH, '//*[@id="AddressStreetModal"]/div/div/div/div[3]/div[1]/div[1]/div[1]/input')
    ADDRESS_INPUT = (By.XPATH, '//*[@id="AddressModal"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input')
    ADDRESS_LIST = (By.XPATH, '//*[@id="AddressModal"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/section/ul')
    ADDRESS_OFFICE = (By.XPATH, '//*[@id="AddressStreetModal"]/div/div/div/div[3]/div[1]/div[2]/div/input')
    COOKIE_FORM = (By.XPATH, '//*[@id="grid"]/div[5]/div')
    OK_COOKIE_BUTTON = (By.XPATH, '//*[@id="grid"]/div[5]/div/div[3]/div[2]/button')
    POPULAR_REQUESTS_LIST = (By.XPATH, '//*[@id="search-popular-requests"]')
    POPULAR_REQUESTS_FIRST = (By.XPATH, '//*[@id="search-popular-requests"]/li[1]')
    RECOMMENDATION_SECOND = (By.XPATH, '//*[@id="searched-results"]/li[2]/div')
    RECOMMENDATION_SHOP = (By.XPATH, '//*[@id="searched-shops"]/li[1]/a')
    SEARCH_STRING = (By.XPATH, '//*[@id="grid"]/header/div/header/div/div[2]/div[1]/div[1]/div/div[2]/input')
    SEARCH_INPUT = (By.XPATH, '//*[@id="grid"]/header/div/header/div/div[2]/div[1]/div[1]/div/div[2]/label')
    SWITCH_TO_SHOPS = (By.XPATH, '//*[@id="js-switcher-shops"]')
    SEARCHED_SHOP_ITEM = (By.XPATH, '//*[@id="searched-shops"]/li/a')

class MainPageLocators():
    ADDRESS_BUTTON = (By.XPATH, '//*[@id="grid"]/header/div/header/div/div[1]/div/div/div[2]')

class CategoryPageLocators():
    SWITCH_TO_PRODUCTS = (By.XPATH, '//*[@id="grid"]/section/div/div/div[5]/div[1]/div/div[2]/span[1]')
    SWITCH_TO_SHOPS = (By.XPATH, '//*[@id="grid"]/section/div/div/div[5]/div[1]/div[1]/div[2]/span[2]')
    
class ResultPageLocators():
    FOUND_MESSAGE = (By.XPATH, '//*[@id="grid"]/section/div/div/div[1]/h1/span')
    NOT_FOUND_MESSAGE = (By.XPATH, '//*[@id="grid"]/section/div/div/div[1]/div/span')
    PRODUCTS_POPUPS = (By.XPATH, '//*[@id="grid"]/section/div/div/div[3]/div[2]/div[2]/div/div[1]/div')
    RECOMMENDATION_MESSAGE = (By.XPATH, '//*[@id="grid"]/section/div/div/div[3]/div[1]/div[1]/b')
    SIMILAR_TAB = (By.XPATH, '//*[@id="grid"]/section/div/div/div[3]/div[2]/div[1]')