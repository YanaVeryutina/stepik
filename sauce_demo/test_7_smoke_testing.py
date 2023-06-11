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
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click login btn')

"""info product 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('select product 1')

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print('open card')

'''info card product 1'''
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('name pass')

cart_price_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print('price pass')

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('click checkout btn')
time.sleep(2)

'''select user info'''
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Anna')
time.sleep(2)
print('enter first name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('ivanova')
time.sleep(2)
print('enter last name')

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('123456')
time.sleep(2)
print('enter postal code')

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
time.sleep(2)

'''finish'''
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('name pass')

finish_price_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]'
                                                       '/div[2]/div')
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('price pass')

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_summary_price = summary_price.text
print(summary_price)
item_total =  'Item total: ' + value_finish_price_product_1
print(item_total)
assert value_summary_price == item_total
time.sleep(2)
print('total price pass')

finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print('finish')
time.sleep(3)



