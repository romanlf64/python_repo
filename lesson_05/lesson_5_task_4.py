from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
sleep(3)
driver.find_element(By.CSS_SELECTOR, '.radius').click()
sleep(5)
print('You logged into a secure area!')
driver.quit()
