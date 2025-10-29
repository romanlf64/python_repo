import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainCalculatorPage import MainCalculatorPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    calc_page = MainCalculatorPage(driver)
    calc_page.open_website()
    calc_page.input_value()
    calc_page.calculator_buttons()
    to_be = calc_page.result()
    
    assert to_be == 15
