from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.MainFormPage import MainFormPage


def test_form():
    browser = webdriver.Edge(service=EdgeService(r"C:\Users\roman\Desktop\msedgedriver.exe"))
    browser.maximize_window()
    page_form = MainFormPage(browser)
    page_form.filling_form('Иван', 'Петров', 'Ленина, 55-3', 'Москва', 'Россия', 'test@skypro.com', 
                           '+7985899998787', 'QA', 'SkyPro')
    page_form.submit_form()
    to_be_one = page_form.check_zip_code_field()
    to_be_two = page_form.check_fields()

    assert to_be_one == 'alert py-2 alert-danger'
    assert to_be_two == 'alert py-2 alert-success'
    
    browser.quit()  
