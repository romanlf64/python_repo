from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
# инициализация драйвера
    driver = webdriver.Edge(service=EdgeService(r"C:\Users\roman\Desktop\msedgedriver.exe"))
    driver.maximize_window()

# открытие страницы
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    
# заполняем форму
    driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
    driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys('SkyPro')

# нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# задаём явное ожидание
    waiter = WebDriverWait(driver, 10)
    waiter.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success"))
    )

# проверяем, что поле zip code подсвечено красным
    zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')
    assert zip_code_field == 'alert py-2 alert-danger'

# проверяем, что остальные поля подсвечены зелёным
    fields = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', 
          '#job-position', '#company']
    for field in fields:
        field_element = driver.find_element(By.CSS_SELECTOR, field).get_attribute('class')
        assert field_element == 'alert py-2 alert-success'

    driver.quit()
