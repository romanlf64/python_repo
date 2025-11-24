import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure


from MainCalculatorPage_10 import MainCalculatorPage


@pytest.fixture()
def driver():
    """
    фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("тестирование калькулятора")
@allure.description("проверка корректности работы калькулятора")
@allure.feature("калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    calc_page = MainCalculatorPage(driver)
    with allure.step("открытие страницы"):
        calc_page.open_website()
    with allure.step("установка значения задержки"):
        calc_page.input_value()
    with allure.step("нажатие кнопок"):
        calc_page.calculator_buttons()
    with allure.step("результат"):
        to_be = calc_page.result()
    with allure.step("проверка результата"):
        assert to_be == 15
