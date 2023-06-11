import time

from selenium import webdriver
from selenium.webdriver import Keys
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
# username.send_keys(Keys.BACKSPACE)
# username.send_keys(Keys.BACKSPACE)
# username.send_keys('er')
password = driver.find_element(By.ID, 'password')
password.send_keys(password_all)
print('input password')
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
filter.click()
print('click filter')
time.sleep(3)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
time.sleep(3)
