from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainFormPage:
    def __init__(self, browser):
        """
        конструктор класса MainFormPage
        :param browser: WebDriver — объект драйвера Selenium
        """
        self.driver = browser
        """
        открытие страницы
        """
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    
    @allure.step("заполнение формы {first_name} {last_name} {address} {city} " \
                 "{country} {e_mail} {phone} {job_position} {company}")
    def filling_form(self, first_name, last_name, address, city, country, 
                     e_mail, phone, job_position, company):
        """
        заполняет форму
        param first_name, last_name, address, city, country, e_mail, 
        phone, job_position, company: str — поля для заполнения
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(e_mail)
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    
    @allure.step("нажатие кнопки")
    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        """
        задание явного ожидания, 10 сек
        """
        waiter = WebDriverWait(self.driver, 10)
        waiter.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger, .alert-success"))
    )
        
    
    @allure.step("проверяем, что поле zip code подсвечено красным")
    def check_zip_code_field(self):
        zip_code_field = self.driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute('class')
        """
        возвращает текущий результат
        """
        return zip_code_field
    
    
    @allure.step("проверяем, что остальные поля подсвечены зелёным")
    def check_fields(self):
        fields = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', 
              '#job-position', '#company']
        for field in fields:
            field_element = self.driver.find_element(By.CSS_SELECTOR, field).get_attribute('class')
        """
        возвращает текущий результат
        """
        return field_element
    