import pytest
import time
import os
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.result_page import ResultPage
from .pages.shop_page import ShopPage
import allure
import allpairspy
from allpairspy import AllPairs

@pytest.mark.chrome
@allure.epic("Chrome tests for Main page")
@allure.parent_suite("Chrome tests for Main page")
@allure.feature("Main page menu")
@allure.suite("Main page menu")
class TestHappyPathChrome():        
    @pytest.mark.search1
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by request in search string")
    def test_search_product_by_request_in_search_string(self, browser_chrome):
        search_request = "чак-чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
            #main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
        with allure.step("Step 3: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_found_message()
            result_page.should_be_recommendation_message(search_request)
            result_page.should_be_products_popups()

    @pytest.mark.search2
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by popular request")
    def test_search_product_by_popular_request(self, browser_chrome):
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: select request"):
            popular_request = main_page.select_popular_request()
            popular_request_text = popular_request.text
        with allure.step("Step 3: start search"):
            main_page.start_search_by_popular_request(popular_request, popular_request_text)
        with allure.step("Step 4: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(popular_request_text)
            result_page.should_be_found_message()
            result_page.should_be_recommendation_message(popular_request_text)
            result_page.should_be_products_popups()

    @pytest.mark.search3
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by text and recommendation")
    def test_search_product_by_text_and_recommendation(self, browser_chrome):
        search_request = "чак-чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text and select recommendation"):
            main_page.insert_search_request(search_request)
            recommendation = main_page.select_recommendation()
            recommendation_text = recommendation.text
        with allure.step("Step 3: start search"):
            main_page.start_search_by_text_and_recommendation(recommendation, recommendation_text)
        with allure.step("Step 4: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(recommendation_text)
            result_page.should_be_any_result_message()
                
    @pytest.mark.search4
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search shop by name in search string")
    def test_search_product_by_name_in_search_string(self, browser_chrome):
        search_request = "многороз"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
        with allure.step("Step 3: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_not_found_message()

    @pytest.mark.search5
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search shop by name and recommendation in search string")
    def test_search_product_by_name_and_recommendation_in_search_string(self, browser_chrome):
        search_request = "многороз"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.insert_search_request(search_request)
            shop_recommendation = main_page.select_shop_recommendation()
            shop_link = shop_recommendation.get_attribute("href")
            shop_recommendation.click()
        with allure.step("Step 3: open shop page"):
            main_page.switch_to_shop_window()
            shop_page = ShopPage(browser_chrome, browser_chrome.current_url)
            shop_page.should_be_shop_in_url(shop_link)

    @pytest.mark.search6
    @allure.story("Address")
    @allure.sub_suite("Address")
    @allure.title("Select address by text")
    def test_select_address_by_text(self, browser_chrome):
        address = "ленина 1"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.open_address_form()
