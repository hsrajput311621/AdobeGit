#CSS Selector

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

# tag&ID , tag&Class, Tag&Attribute, Tag,Attribute and Class

driver.find_element(By.CSS_SELECTOR,"")
