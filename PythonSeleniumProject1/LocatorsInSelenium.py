
# Locators in the Selenium:

# ID, Name, Link Text or Partial Link Text, Class Name, Tag Name

# Customise Locators: CSS Selector(Tag and ID, Tag and Class, Tag and Attribute, Tag, Class and Attribute)
# and Xpath(Absolute and Relative Xpath)
#  Element(Tag Name)  Attribute       Value
# e.g <input             name=     "txtUsername" id="txtUsername" type="text"

'''from selenium import webdriver

from selenium.webdriver.chrome.service import Service

serv_obj=Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(serv_obj)
'''
''' The below code is good for Selenium 3

from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\Web-Driver\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.find_element_by_name("txtUsername").send_keys("Admin")

driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

act_title=driver.title
extpected_title="OrangeHRM"
    
if act_title==extpected_title:
    print("Test is passed")
else:
    print("test is failed")

driver.close()
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("D:\Web-Driver\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
#driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element(By.NAME,"txtUsername" ).send_keys("Admin")
#driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element(By.ID,"txtPassword" ).send_keys("admin123")
#driver.find_element_by_id("btnLogin").click()   (in selenium 3)
driver.find_element(By.ID, "btnLogin").click()
print(driver.current_url)
act_title = driver.title
extpected_title = "OrangeHRM"
if act_title == extpected_title:
    print("Test is passed")
else:
    print("test is failed")
driver.close()