import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.LoginShopPage import LoginShopPage
from pages.MainShopPage import MainShopPage
from pages.CartShopPage import CartShopPage
from pages.FormShopResultPage import FormShopResultPage

@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop(driver):
    login_page = LoginShopPage(driver)
    login_page.open_website()
    login_page.authorization('standard_user', 'secret_sauce')
    login_page.submit()
    main_page = MainShopPage(driver)
    main_page.add_items_to_cart()
    main_page.go_to_cart()
    cart_page = CartShopPage(driver)
    cart_page.submit_checkout()
    form_result_page = FormShopResultPage(driver)
    form_result_page.form_page('Леонид', 'Романов', '636840')
    form_result_page.submit_continue()
    to_be = form_result_page.check_total_price()
    
    assert to_be == "Total: $58.29"
