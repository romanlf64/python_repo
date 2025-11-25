from selenium.webdriver.common.by import By
import allure


class LoginShopPage:


    def __init__(self, driver):
        """
        коструктор класса LoginShopPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver


    @allure.step("открытие страницы регистрации")
    def open_website(self):
        self.driver.get('https://www.saucedemo.com/')


    @allure.step("авторизация {Username} {Password}")
    def authorization(self, Username, Password):
        """
        авторизация на сайте
        :param Username: str - логин
        :param Password: str - пароль
        """
        user_name = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name.clear()
        user_name.send_keys(Username)
        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.clear()
        password.send_keys(Password)
        

    @allure.step("нажатие кнопки Login")
    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        