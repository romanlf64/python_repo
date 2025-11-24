from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainShopPage:


    def __init__(self, driver):
        """
        конструктор класса MainShopPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    
    @allure.step("добавление выбранных товаров в корзину")
    def add_items_to_cart(self):
        """
        добавление товаров в корзину нажатием кнопок Add to cart
        """
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()


    @allure.step("переход в корзину путём нажатия на иконку корзины")
    def go_to_cart(self):
        """
        установка явного ожидания 5 сек для отображения количества
        выбранных товаров на иконке корзины
        """
        waiter = WebDriverWait(self.driver, 5)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.shopping_cart_badge'), '3')
        )
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
        