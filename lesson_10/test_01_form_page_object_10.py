from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import allure


from MainFormPage_10 import MainFormPage


@allure.title("тестирование формы")
@allure.description("тест проверяет корректность работы формы при заполнении "
                    "её полей данными")
@allure.feature("форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form():
    with allure.step("инициализация драйвера"):
        browser = webdriver.Edge(service=EdgeService(r"C:\Users\roman\Desktop\msedgedriver.exe"))
    browser.maximize_window()
    page_form = MainFormPage(browser)
    with allure.step("заполнение полей формы данными"):
        page_form.filling_form('Иван', 'Петров', 'Ленина, 55-3', 'Москва', 'Россия', 
                               'test@skypro.com', '+7985899998787', 'QA', 'SkyPro')
    with allure.step("нажатие кнопки submit"):
        page_form.submit_form()
    with allure.step("проверяем, что поле zip code подсвечено красным"):
        to_be_one = page_form.check_zip_code_field()
    with allure.step("проверяем, что остальные поля подсвечены зелёным"):
        to_be_two = page_form.check_fields()
    with allure.step("проверка результата"):
        assert to_be_one == 'alert py-2 alert-danger'
        assert to_be_two == 'alert py-2 alert-success'
    
    browser.quit() 
    