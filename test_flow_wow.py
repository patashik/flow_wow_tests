import pytest
import time
import os
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.result_page import ResultPage
import allure
import allpairspy
from allpairspy import AllPairs

@pytest.mark.chrome
@allure.epic("Chrome tests for Main page")
@allure.parent_suite("Chrome tests for Main page")
@allure.feature("Main page menu")
@allure.suite("Main page menu")
class TestHappyPathChrome():        
    @pytest.mark.search
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by text request in products")
    def test_search_product_by_request_in_products(self, browser_chrome):
        search_request = "чак-чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
        with allure.step("Step 3: show search results in products"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_results_in_menu(search_request)
            result_page.should_be_products_popups()
            result_page.should_be_suggestions(search_request)

    @pytest.mark.search
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by text request in shops")
    def test_search_product_by_request_in_shops(self, browser_chrome):
        search_request = "чак-чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
        with allure.step("Step 3: show search results in products"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_results_in_menu(search_request)
            result_page.should_be_products_popups()
            result_page.should_be_suggestions(search_request)
        with allure.step("Step 4: switch to shops"):
            result_page.should_switch_to_shops()
        with allure.step("Step 5: show search results in shops"):
            result_page.should_be_search_results_in_menu(search_request)
            result_page.should_be_shops_popups()