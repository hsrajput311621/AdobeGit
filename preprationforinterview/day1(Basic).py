# Testcase:
"""
This is a comment
written in
more than just one line
"""
#Open WEb Browser
#Open URL(opensource-demo.orangehrmlive.com)
#Provide Email
#Provide password
#click on login
#Capture title of the dashboard page
#Verify title of teh page
#close browser.
# webdriver is a module and now by importing we can use all the class and the objects.

# The below is the method of Selenium 3 :
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
actual_title = "Swag Labs"
expected_title = driver.title
print(expected_title)
if expected_title == actual_title:
    print("The test is passed the Expected result is same as actual result")
else:
    print("The test failed")
time.sleep(2)

print("Adding the product into the cart")

driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
## This statment will us to scroll down the entire screen to down

time.sleep(2)

driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()

time.sleep(2)

driver.find_element(By.XPATH , "//a[@class='shopping_cart_link']").click()

time.sleep(2)

driver.find_element(By.ID,"checkout").click()

time.sleep(2)

driver.find_element(By.ID,"first-name").send_keys("Hitesh")

driver.find_element(By.ID,"last-name").send_keys("Rajput")

driver.find_element(By.ID,"postal-code").send_keys("110030")

time.sleep(2)

driver.find_element(By.ID,"continue").click()

time.sleep(2)

driver.find_element(By.ID,"finish").click()

time.sleep(2)

driver.find_element(By.NAME, "back-to-products").click()

time.sleep(2)

driver.close()

# #From the webdriver module we import the Chorme class and created a object driver and now by the help of chrome class
# #driver we can perform all the function related to website on the chorme.
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# # driver.maximize_window()
# #print(driver.current_url)
# # driver.find_element(By.NAME,"username").send_keys("Admin")
# # driver.find_element(By.NAME,"password").send_keys("admin123")
# # driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
# driver.find_element_by_name("username").send_keys("Admin")
# # driver.find_element(by=By.NAME, value=username).send_keys("Admin")
# driver.find_element_by_name("password").send_keys("admin123")
# driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
# actual_title = "OrangeHRM"
# expected_title = driver.title
# print(expected_title)
# if expected_title == actual_title:
#     print("The test is passed the Expected result is same as actual result")
# else:
#     print("The test failed")
#











