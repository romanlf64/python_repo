import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from LoginShopPage_10 import LoginShopPage
from MainShopPage_10 import MainShopPage
from CartShopPage_10 import CartShopPage
from FormShopResultPage_10 import FormShopResultPage
import allure


@pytest.fixture()
def driver():
    """
    фикстура инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("тестирование интернет-магазина")
@allure.description("проверка корректности работы интернет-магазина при "
                    "оформлении заказа")
@allure.feature("интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    login_page = LoginShopPage(driver)
    with allure.step("открытие сайта"):
        login_page.open_website()
    with allure.step("авторизация"):
        login_page.authorization('standard_user', 'secret_sauce')
    with allure.step("нажатие кнопки"):
        login_page.submit()
    main_page = MainShopPage(driver)
    with allure.step("добавление товаров в корзину"):
        main_page.add_items_to_cart()
    with allure.step("переход в корзину"):
        main_page.go_to_cart()
    cart_page = CartShopPage(driver)
    with allure.step("нажатие кнопки Checkout"):
        cart_page.submit_checkout()
    form_result_page = FormShopResultPage(driver)
    with allure.step("заполнение формы"):
        form_result_page.form_page('Леонид', 'Романов', '636840')
    with allure.step("нажатие кнопки Continue"):
        form_result_page.submit_continue()
    with allure.step("итоговая стоимость"):
        to_be = form_result_page.check_total_price()
    with allure.step("проверка итоговой стоимости товаров"):
        assert to_be == "Total: $58.29"
    