from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

obj_serv = Service("D:\Web-Driver\chromedriver.exe")

driver = webdriver.Chrome(service=obj_serv)

driver.get("https://elearning.adobe.com/")
driver.maximize_window()
print(driver.current_url)
driver.find_element(By.XPATH, "//a[@class='cp-login-button']").click()
driver.find_element(By.ID, "EmailPage").send_keys("hiteshr@adobe.com")
# # driver.find_element(By.XPATH, "//span[@class='spectrum-Button-label']").click()
# driver.find_element(By.XPATH, "//div[contains(text(),'Personal Account')]").click()
# driver.find_element(By.XPATH, "//input[@id='PasswordPage-PasswordField']").send_keys("Adobe@2022")
# driver.find_element(By.XPATH, "//span[@class='spectrum-Button-label']").click()
title_name= print(driver.title)
if title_name == "Elearning Home - eLearning":
    print("the title name is correct")
else:
    print("there is a problem in the link")

driver.quit()
