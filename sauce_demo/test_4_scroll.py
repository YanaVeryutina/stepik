import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('input password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('click login btn')
time.sleep(5)

# driver.execute_script('window.scrollTo(0, 500)')

action = ActionChains(driver)
baby_shirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
action.move_to_element(baby_shirt).perform()

time.sleep(3)


now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M')
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('C:\\Users\\veryu\\PycharmProjects\\stepik\\screenshots\\' + name_screenshot)


