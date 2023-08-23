
# Class name is used to search more than one locator, as name, ID can be unique but Class name
# is not unique, some time more than one elements can be inside one class.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\drivers\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

print(driver.current_url)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

print(driver.title)

# #slider=driver.find_elements(By.CLASS_NAME,"homeslider-description")
#
# print(len(slider))
#
# links = driver.find_elements(By.TAG_NAME,"a")
#
# print(len(links))

driver.close()