import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)


check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()
time.sleep(2)

check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
check_box.click()

