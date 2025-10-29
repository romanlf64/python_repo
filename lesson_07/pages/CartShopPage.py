from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartShopPage:

    def __init__(self, driver):
        self.driver = driver

    def submit_checkout(self):
        # нажимаем Checkout, предварительно задав явное ожидание
        waiter = WebDriverWait(self.driver, 5)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'button#checkout'), 'Checkout')
        )
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        