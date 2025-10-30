from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainFormPage:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


    def filling_form(self, first_name, last_name, address, city, country, e_mail, phone, job_position, company):
        # заполняем форму
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(e_mail)
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit_form(self):
        # нажимаем кнопку
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        # задаём явное ожидание
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success"))
    )
        
    def check_zip_code_field(self):
        # проверяем, что поле zip code подсвечено красным
        zip_code_field = self.driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')
        return zip_code_field
    
    def check_fields(self):
        # проверяем, что остальные поля подсвечены зелёным
        fields = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', 
              '#job-position', '#company']
        for field in fields:
            field_element = self.driver.find_element(By.CSS_SELECTOR, field).get_attribute('class')
        return field_element

    

        