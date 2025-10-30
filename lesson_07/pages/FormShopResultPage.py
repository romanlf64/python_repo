from selenium.webdriver.common.by import By

class FormShopResultPage:

    def __init__(self, driver):
        self.driver = driver

    def form_page(self, firstName, lastName, postCode):
        # заполняем форму своими данными
        first_name = self.driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.clear()
        first_name.send_keys(firstName)
        last_name = self.driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.clear()
        last_name.send_keys(lastName)
        post_code = self.driver.find_element(By.CSS_SELECTOR, '#postal-code')
        post_code.clear()
        post_code.send_keys(postCode)

    def submit_continue(self):
        # нажимаем Continue
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def check_total_price(self):
        # читаем итоговую стоимость товаров
        total_price = self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        
        return total_price
    