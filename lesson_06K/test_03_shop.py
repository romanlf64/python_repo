import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_labs(driver):
# открываем сайт
    driver.get('https://www.saucedemo.com/')
# авторизуемся
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name.clear()
    user_name.send_keys('standard_user')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.clear()
    password.send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
# добавляем товары в корзину
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
# переходим в корзину
    driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
# нажимаем Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()
# заполняем форму своими данными
    first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
    first_name.clear()
    first_name.send_keys('Леонид')
    last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
    last_name.clear()
    last_name.send_keys('Романов')
    post_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    post_code.clear()
    post_code.send_keys('636840')
# нажимаем Continue
    driver.find_element(By.CSS_SELECTOR, '#continue').click()
# читаем итоговую стоимость товаров
    total_price = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
# проверяем, что итоговая сумма равна "Total: $58.29"
    assert total_price == "Total: $58.29"
