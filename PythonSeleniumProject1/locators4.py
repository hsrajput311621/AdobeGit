
# Link text and Partial link text

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.LINK_TEXT,"Register").click()

