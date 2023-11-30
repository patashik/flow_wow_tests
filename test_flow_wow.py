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
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_sidebar_name(search_request)
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
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_sidebar_name(search_request)
            result_page.should_be_shops_popups()

    @pytest.mark.rec
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by suggestion in products")
    def test_search_product_by_suggestion_in_products(self, browser_chrome):
        search_request = "чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
        with allure.step("Step 2: insert text in string"):
            main_page.insert_search_request(search_request)
        with allure.step("Step 3: list suggestions"):
            main_page.list_suggestions()
        with allure.step("Step 4: select suggestion and start search"):
            suggestion = main_page.select_single_suggestion()
            suggestion_text = suggestion.text
            suggestion.click()
        with allure.step("Step 5: show search results in products"):
            main_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_fields(suggestion_text)
            result_page.should_be_products_popups()
        with allure.step("Step 6: select recommendation and start search"):
            result_page.search_by_recommendation()
            result_page.should_be_products_popups()

