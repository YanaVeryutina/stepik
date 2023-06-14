import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)


radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radio_button.click()
time.sleep(2)



