from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, 'input#newButtonName').send_keys('SkyPro')
button = driver.find_element(By.CSS_SELECTOR, 'div.form-group')
button.find_element(By.CSS_SELECTOR, '[type="button"]').click()
print(button.find_element(By.CSS_SELECTOR, '[type="button"]').text)

driver.quit()
