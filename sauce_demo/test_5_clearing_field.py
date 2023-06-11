import datetime
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

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys(login_standard_user)
print('input login')
time.sleep(5)

username.clear()

# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print('input password')
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print('click login btn')
# time.sleep(5)

time.sleep(5)



