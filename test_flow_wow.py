import pytest
import time
import os
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.result_page import ResultPage
from .pages.shop_page import ShopPage
from .pages.category_page import CategoryPage
import allure

@pytest.mark.chrome
@allure.epic("Chrome tests for Main page")
@allure.parent_suite("Chrome tests for Main page")
@allure.feature("Main page menu")
@allure.suite("Main page menu")
class TestHappyPathChrome():        
    @pytest.mark.search1
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search product by text")
    def test_search_product_by_text(self, browser_chrome):
        search_request = "чак-чак"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
            #main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
            main_page.should_change_url()
            main_page.should_be_search_request_in_url(search_request)
        with allure.step("Step 3: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_found_message()
            result_page.should_be_recommendation_message(search_request)
            result_page.should_be_products_popups()

    @pytest.mark.pop
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
            popular_request.click()
            main_page.should_change_url()
            main_page.should_be_search_request_in_url(popular_request_text)
        with allure.step("Step 4: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(popular_request_text)
            result_page.should_be_found_message()
            result_page.should_be_recommendation_message(popular_request_text)
            result_page.should_be_products_popups()

    @pytest.mark.rec
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
            recommendation.click()
            main_page.should_change_url()
            main_page.should_be_search_request_in_url(recommendation_text)
        with allure.step("Step 4: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(recommendation_text)
            result_page.should_be_any_result_message()
                
    @pytest.mark.shop
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search shop by name")
    def test_search_shop_by_name(self, browser_chrome):
        search_request = "многороз"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text in string and activate search"):
            main_page.start_search_by_request(search_request)
            main_page.should_change_url()
            main_page.should_be_search_request_in_url(search_request)
        with allure.step("Step 3: show search results"):
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_be_not_found_message()

    @pytest.mark.shop2
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search shop by name and recommendation")
    def test_search_product_by_name_and_recommendation(self, browser_chrome):
        search_request = "многороз"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: insert text in string"):
            main_page.insert_search_request(search_request)
        with allure.step("Step 3: select recommendation and activate search"):
            shop_recommendation = main_page.select_shop_recommendation()
            shop_link = shop_recommendation.get_attribute("href")
            shop_recommendation.click()
        with allure.step("Step 3: open shop page"):
            main_page.switch_to_shop_window()
            shop_page = ShopPage(browser_chrome, browser_chrome.current_url)
            shop_page.should_be_content_in_url(shop_link)

    @pytest.mark.address
    @allure.story("Address")
    @allure.sub_suite("Address")
    @allure.title("Set address")
    def test_set_address(self, browser_chrome):
        address = "улица Ленина"
        house = "1"
        office = "1"
        comment = "test"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: set address using dropdown list"):
            main_page.click_set_address()
            main_page.should_open_address_form()
            main_page.insert_address(address)
            main_page.select_address_from_list(address)
        with allure.step("Step 3: set detailed address"):
            main_page.fill_detailed_address_form(house, office, comment)
            main_page.should_disappear_detailed_address_form()
            main_page.should_be_setted_address(address, house)

    @pytest.mark.cart
    @allure.story("Cart")
    @allure.sub_suite("Cart")
    @allure.title("Add product to cart")
    def test_add_product_to_cart(self, browser_chrome):
        address = "улица Ленина, 1"
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: open flowers category page"):
            main_page.go_to_category_page()
            main_page.should_change_url()
            main_page.should_open_category_page()
            category_page = CategoryPage(browser_chrome, browser_chrome.current_url)
        with allure.step("Step 3: switch to product subcategory"):
            #category_page.switch_to_subcategory()
            subcategory_link = category_page.get_subcategory_link()
            subcategory_title = category_page.get_subcategory_title()
            #time.sleep(7)
            category_page.click_subcategory()
            category_page.should_change_url()
            category_page.should_be_correct_url(subcategory_link)
            category_page.should_be_correct_page_topic(subcategory_title)
        with allure.step("Step 4: select product"):
            product_name = category_page.get_product_name()
            product_link = category_page.get_product_link()
            category_page.click_product()
            category_page.should_change_url()
            category_page.should_be_correct_url(product_link)
            category_page.should_be_correct_card_title(product_name)
        with allure.step("Step 5: add product to cart"):
            category_page.add_to_cart()
        with allure.step("Step 6: set address"):
            category_page.fill_short_address_form(address)
            category_page.should_disappear_address_form()
        with allure.step("Step 7: go to shop page with cart"):
            category_page.should_change_url()
            category_page.should_open_shop_page()
            shop_page = ShopPage(browser_chrome, browser_chrome.current_url)
            shop_page.should_be_cart()
            shop_page.should_be_product_in_cart(product_name)
        with allure.step("Step 8: go to make order"):
            shop_page.go_to_make_order()
        with allure.step("Step 9: open login form"):
            shop_page.should_open_login_form()

    @pytest.mark.resize1
    @allure.story("Resize window")
    @allure.sub_suite("Resize window")
    @allure.title("Resize window on main page")
    def test_resize_main_page(self, browser_chrome):
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = MainPage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
            #main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: resize window"):
            width = 800
            height = 600
            main_page.resize_window(width, height)
        with allure.step("Step 3: maximize window"):
            main_page.maximize_window()
        with allure.step("Step 4: click logo to reload main page"):
            main_page.go_to_main_page()
            #main_page.should_change_url()
            main_page.should_open_main_page()

    @pytest.mark.resize2
    @allure.story("Resize window")
    @allure.sub_suite("Resize window")
    @allure.title("Resize window on category page")
    def test_resize_category_page(self, browser_chrome):
        link = "https://flowwow.com/kazan/" 
        with allure.step("Step 1: open category page"):
            category_page = CategoryPage(browser_chrome, link)
            category_page.open()
            category_page.accept_cookies()
            #category_page.should_be_correct_response_status_code()
        with allure.step("Step 2: resize window"):
            width = 800
            height = 600
            category_page.resize_window(width, height)
            time.sleep(2)
        with allure.step("Step 3: maximize window"):
            category_page.maximize_window()
        with allure.step("Step 4: click logo and go to main page"):
            category_page.go_to_main_page()
            category_page.should_change_url()
            category_page.should_open_main_page()
    
    @pytest.mark.resize3
    @allure.story("Resize window")
    @allure.sub_suite("Resize window")
    @allure.title("Resize window on shop page")
    def test_resize_shop_page(self, browser_chrome):
        link = "https://flowwow.com/shop/mnogoroz/" 
        with allure.step("Step 1: open shop page"):
            shop_page = ShopPage(browser_chrome, link)
            shop_page.open()
            #shop_page.should_be_correct_response_status_code()
        with allure.step("Step 2: resize window"):
            width = 800
            height = 600
            shop_page.resize_window(width, height)
        with allure.step("Step 3: maximize window"):
            shop_page.maximize_window()
        with allure.step("Step 4: click logo and go to start page"):
            shop_page.go_to_main_page_from_shop_page()
            shop_page.should_change_url()
            print(shop_page.browser.current_url)
            shop_page.should_open_start_page()
            
    @pytest.mark.time
    @allure.story("Time")
    @allure.sub_suite("Time")
    @allure.title("Set time")
    def test_set_time(self, browser_chrome):
        link = "https://flowwow.com/kazan/all-products/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.accept_cookies()
        with allure.step("Step 2: set time using allpairs"):
            main_page.click_time_settings()
            main_page.should_open_time_form()
            main_page.set_time(time)
            main_page.should_be_setted_time()