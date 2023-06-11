from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# s = Service('C:\\Users\\veryu\\PycharmProjects\\stepik\\geckodriver.exe')
# driver = webdriver.Firefox(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')
button_login = driver.find_element(By.ID, "login-button")
button_login.click()


# driver.close()

