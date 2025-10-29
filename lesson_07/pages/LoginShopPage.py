from selenium.webdriver.common.by import By

class LoginShopPage:

    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        # открываем сайт
        self.driver.get('https://www.saucedemo.com/')

    def authorization(self, Username, Password):
        # авторизуемся
        user_name = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name.clear()
        user_name.send_keys(Username)
        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.clear()
        password.send_keys(Password)
        
    def submit(self):
        # нажимаем кнопку 'Login'
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
