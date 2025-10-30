from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainCalculatorPage:


    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        # открытие страницы
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        
    def input_value(self):
        # в поле ожидания вводим значение 45, предварительно очистив его
        field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        field.clear()
        field.send_keys('45')

    def calculator_buttons(self):
        # нажимаем "7", "+", "8", "="
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()
        # задаём явное ожидание
        waiter = WebDriverWait(self.driver, 46)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

    def result(self):
        # проверяем, что в окне через 45 секунд отобразится число 15
        txt = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        
        return int(txt)