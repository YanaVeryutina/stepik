import datetime
import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('/chromedriver.exe')
driver = webdriver.Chrome(service=s)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)


new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# new_date.send_keys('06/12/2023')
# time.sleep(2)
# new_date.send_keys(Keys.RETURN)
# time.sleep(2)

new_date.click()
# time.sleep(3)
# date_tomorrow = driver.find_element(By.XPATH, "//div[@aria-label='Choose Thursday, June 15th, 2023']")
# date_tomorrow.click()
# time.sleep(3)

# today_date = driver.find_element(By.XPATH, "//div[contains(@class='react-datepicker__day--today')]")
# today_date.click()


now_date = datetime.datetime.utcnow().strftime('%d')
date = int(now_date) + 1
print(date)
locator = "//div[@aria-label='Choose Thursday, June " + str(date) + "th, 2023']"
print(locator)

tomorrow_date = driver.find_element(By.XPATH, locator)
tomorrow_date.click()