

# Date Picker:
#1) Standard
#2) Non- Standard(Customized)

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.switch_to.frame(0)

#driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("10/30/2022")

year = "2023"
month = "January"
date = "9"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month == mon and year == yr:
        break;
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break

time.sleep(5)

#driver.close()

