import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

username = driver.find_element(By.ID, 'user-name')
username.send_keys(login_standard_user)
print('input login')
password = driver.find_element(By.ID, 'password')
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print('click login btn')

warning_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warning_text = warning_text.text
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'

driver.refresh()
