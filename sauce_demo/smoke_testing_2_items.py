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

'''fill login form'''
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys(login_standard_user)
print('input login')
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click login button')

'''info product 1'''
product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_1 = product_1.text
print(f'name of product 1 {value_product_1}')

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(f'price of product 1 {value_price_product_1}')

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_1.click()
print('select product 1')

'''info product 2'''
product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_product_2 = product_2.text
print(f'name of product 2 {value_product_2}')

price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(f'price of product 2 {value_price_product_2}')

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
select_product_2.click()
print('select product 2')

'''move to card '''
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print('open card')

'''info card product 1'''
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_cart_product_1 = cart_product_1.text
print(f'name of product 1 in card {value_cart_product_1}')
assert value_product_1 == value_cart_product_1
print('name product 1 pass')

cart_price_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]'
                                                     '/div[4]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text
print(f'price of product 1 in card {value_cart_price_product_1}')
assert value_price_product_1 == value_cart_price_product_1
print('price product 1 pass')

'''info card 2'''
cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_cart_product_2 = cart_product_2.text
print(f'name of product 2 in card {value_cart_product_2}')
assert value_product_2 == value_cart_product_2
print('name product 2 pass')

cart_price_product_2 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]'
                                                     '/div[4]/div[2]/div[2]/div')
value_cart_price_product_2 = cart_price_product_2.text
print(f'price of product 2 in card {value_cart_price_product_2}')
assert value_price_product_2 == value_cart_price_product_2
print('price product 2 pass')

'''checkout items'''
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('click checkout button')

'''select user info'''
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('ivanna')
print('enter first name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('ivanova')
print('enter last name')

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('123456')
print('enter postal code')

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('click on continue button')

'''checkout product 1'''
checkout_product_1 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_checkout_product_1 = checkout_product_1.text
print(f'name of product 1 on checkout page {value_checkout_product_1}')
assert value_product_1 == value_checkout_product_1
print('name for product 1 pass')

checkout_price_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]'
                                                         '/div[3]/div[2]/div[2]/div')
value_checkout_price_product_1 = checkout_price_product_1.text
print(f'price of product 1 on checkout page {value_checkout_price_product_1}')
assert value_price_product_1 == value_checkout_price_product_1
print('price for product 1 pass')

'''checkout product 2'''
checkout_product_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_checkout_product_2 = checkout_product_2.text
print(f'name of product 2 on checkout page {value_checkout_product_2}')
assert value_product_2 == value_checkout_product_2
print('name for product 2 pass')

checkout_price_product_2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]'
                                                         '/div[4]/div[2]/div[2]/div')
value_checkout_price_product_2 = checkout_price_product_2.text
print(f'price of product 2 on checkout page {value_checkout_price_product_2}')
assert value_price_product_2 == value_checkout_price_product_2
print('price for product 2 pass')

'''get summary price'''
summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_summary_price = summary_price.text
print(f'summary price: {summary_price}')

new_value_price_product_1 = value_checkout_price_product_1.replace('$', '')
new_value_price_product_2 = value_checkout_price_product_2.replace('$', '')

total_price_for_two_items = float(new_value_price_product_1) + float(new_value_price_product_2)

item_total = 'Item total: ' + '$' + str(total_price_for_two_items)
print(item_total)
assert value_summary_price == item_total
print('total price for two items pass')

finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print('click on finish button')
