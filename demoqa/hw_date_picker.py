import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)


date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date.click()

'''Choose date in the future'''
now_date = datetime.datetime.utcnow().strftime('%d')
date = int(now_date) + 10
print(f'New date is: {date}')
locator = "//div[@aria-label='Choose Saturday, June " + str(date) + "th, 2023']"
print(f'New locator is: {locator}')

'''Press on new date'''
date_in_future = driver.find_element(By.XPATH, locator)
date_in_future.click()
print('successful click')

expected_date = '06/24/2023'
actual_result = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]').text
print(actual_result)
# assert actual_result == expected_date, f'Failed. Expected  is {expected_date}, but got {actual_result}'
# print('test pass')
