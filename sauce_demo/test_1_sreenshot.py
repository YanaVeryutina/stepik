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

username = driver.find_element(By.ID, 'user-name')
username.send_keys(login_standard_user)
print('input login')
password = driver.find_element(By.ID, 'password')
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print('click login btn')
time.sleep(5)
# text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == 'Products'
# print('Pass')

# now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M')
# name_screenshot = 'screenshot' + now_date + '.png'
# driver.save_screenshot('C:\\Users\\veryu\\PycharmProjects\\stepik\\screenshots\\' + name_screenshot)

# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
#
# print('Correct URL')

