from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainCalculatorPage:


    def __init__(self, driver):
        """
        конструктор класса MainCalculatorPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    
    @allure.step("открытие страницы сайта")
    def open_website(self):
        """
        открывает страницу Slow calculator
        """
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        
    
    @allure.step("установка значения задержки в секундах в поле ожидания")
    def input_value(self):
        field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        field.clear()
        field.send_keys('45')

    
    @allure.step('поочерёдное нажатие кнопок "7", "+", "8", "=" и явное ожидание 46 сек')
    def calculator_buttons(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

        """
        задаём явное ожидание
        """
        waiter = WebDriverWait(self.driver, 46)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    
    @allure.step("проверяем, что в окне через 45 секунд отобразится число 15")
    def result(self):
        # проверяем, что в окне через 45 секунд отобразится число 15
        txt = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        """
        возвращает текущий результат 
        """
        return int(txt)
    