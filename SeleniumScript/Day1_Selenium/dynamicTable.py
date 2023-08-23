

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

# Total number of rows:

rows = len(driver.find_elements(By.XPATH, "//table[@id = 'resultTable']//tbody/tr"))
print("Total number of rows in the table is ", rows)

count = 0
for r in range(1, rows+1):
    status = driver.find_element(By.XPATH, "//table[@id = 'resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status == "Enabled":
        count = count + 1

print("Number of enalbed users", rows)
print("Number of enabled users", count)
print("Number of disabled users", rows - count)

driver.close()

