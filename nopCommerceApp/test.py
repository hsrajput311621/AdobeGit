import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
# act_title = driver.title
# print(act_title)

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").send_keys("admin")

time.sleep(2)

actual_title = driver.title
time.sleep(2)

if actual_title == "Dashboard / nopCommerce administration":

    print(actual_title, "The test is passed")
else:

    print(actual_title, "The test is failed")

driver.close()

