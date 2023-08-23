
# Date Picker:
#1) Standard
#2) Non- Standard(Customized)

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.XPATH, "//input[@id = 'dob']").click()

datepicker_month =Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Oct")

datepicker_year =Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1991")

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in dates:
    if date == "30":
        date.click()
        break

time.sleep(5)

driver.close()

