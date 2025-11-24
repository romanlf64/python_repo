from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartShopPage:


    def __init__(self, driver):
        """
        конструктор класса CartShopPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver


    @allure.step("нажатие кнопки Checkout")
    def submit_checkout(self):
        """
        установка явного ожидания 5 сек
        """
        waiter = WebDriverWait(self.driver, 5)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button#checkout'), 'Checkout')
        )
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
