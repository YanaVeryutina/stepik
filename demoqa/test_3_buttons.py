import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)

action = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
time.sleep(2)

right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
time.sleep(2)


