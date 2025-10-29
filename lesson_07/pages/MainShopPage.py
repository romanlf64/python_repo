from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainShopPage:

    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self):
        # добавляем товары в корзину
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        # переходим в корзину, предварительно задав явное ожидание
        waiter = WebDriverWait(self.driver, 5)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.shopping_cart_badge'), '3')
        )
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        