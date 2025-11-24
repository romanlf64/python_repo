from selenium.webdriver.common.by import By
import allure


class FormShopResultPage:


    def __init__(self, driver):
        """
        конструктор класса FormShopResultPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver

    @allure.step("заполнение формы данными {firstName} {lastName} {postCode}")
    def form_page(self, firstName, lastName, postCode):
        """
        заполнение полей формы данными
        :param firstName: str - имя
        :param lastName: str - фамилия
        :param postCode: str - индекс
        """
        first_name = self.driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.clear()
        first_name.send_keys(firstName)
        last_name = self.driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.clear()
        last_name.send_keys(lastName)
        post_code = self.driver.find_element(By.CSS_SELECTOR, '#postal-code')
        post_code.clear()
        post_code.send_keys(postCode)


    @allure.step("нажатие кнопки Continue")
    def submit_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("чтение итоговой стоимости товаров")
    def check_total_price(self):
        total_price = self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        """
        возвращает итоговую стоимость товаров
        """
        return total_price
    