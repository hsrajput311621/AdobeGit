

# checkboxes #
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://itera-qa.azurewebsites.net/home/automation")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(1)

checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@id, 'day')]")

print(len(checkboxes)) #7

# approach1 we can use range function in the for loop

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

time.sleep(1)

# here we cal also use simple for loop for clicking:

# for checkbox in checkboxes:
#     checkbox.click()

time.sleep(2)

#Select multiple checkboxes with our choice

# for checkbox in checkboxes:
#     weekday = checkboxe.get_attribute('id')
#     if weekday == 'monday' or weekday == 'sunday':
#         checkbox.click()

time.sleep(2)

#4 select last n checkboxes:
# range(5,7) -->6,7
# totalnumberofelements-2 = starting index
for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()

#5) select first 2 checkboxes:
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

#6_ clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


driver.quit()