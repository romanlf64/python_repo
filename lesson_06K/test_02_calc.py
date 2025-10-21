from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
# инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

# открытие страницы
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

# в поле ожидания вводим значение 45, предварительно очистив его
    field = driver.find_element(By.CSS_SELECTOR, '#delay')
    field.clear()
    field.send_keys('45')

# нажимаем "7", "+", "8", "="
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

# задаём явное ожидание
    waiter = WebDriverWait(driver, 46)
    waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))

# проверяем, что в окне через 45 секунд отобразится число 15
    txt = driver.find_element(By.CSS_SELECTOR, '.screen').text
    assert int(txt) == 15

    driver.quit()
