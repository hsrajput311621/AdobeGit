#Test Case
#1) Open the browser : https://opensource-demo.orangehrmlive.com/.
#2) Login to the website by using credentials.
#3) usernmae  = Admin
#4) Password = admin123
#5) capture the title of the website (Actual)
#6) Compare the title with the expected title of the page(Expected).
#7) close the browser.

#This below code is dedicated to selenium 3
# from selenium import webdriver
#
# #driver is an object of Chrome Class, which is use to call the class, and Chrome is a class in selenium.
#
# driver = webdriver.Chrome(executable_path="D:\Web-Driver\chromedriver.exe")
# driver = webdriver.Chrome()
#
# #we may not use executable_path in Selenium 4, till selenium 3 it was working file.
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# driver.maximize_window()
#
# driver.current_url
#
# driver.find_element_by_id("txtUsername").send_keys("Admin")
#
# driver.find_element_by_id("txtPassword").send_keys("admin123")
#
# driver.find_element_by_id("btnLogin").click()
#
# act_title = driver.title
#
# exp_title = "OrangeHRM"
#
# if (act_title == exp_title):
#     print("The Title Test case passed")
# else:
#     print("The Title test case does not passed")
#
# driver.close()

# -----------------------------------------------------------------------------------------#

# This below code is Selenium 4



# In selenium we have sub module called "webdriver", inside webdriver we have "chrome" class, inside chrome we have "service" class from service class we need to import Service.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#obj_serv = Service("D:\Web-Driver\chromedriver.exe")

#obj_serv is an object of Service class, which is use to call the class, and Chrome is a class in selenium.

#driver = webdriver.Chrome(service=obj_serv)

driver = webdriver.Chrome()    # This is the shortcut the  for webdriver we need to copy the chrmoe in python script location.

#we may not use executable_path in Selenium 4, till selenium 3 it was working file.

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.current_url

#driver.find_element_by_id("txtUsername").send_keys("Admin")

driver.find_element(By.ID, "txtUsername" ).clear()

driver.find_element(By.ID, "txtUsername" ).send_keys("Admin")

#driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element(By.ID, "txtPassword" ).clear()

driver.find_element(By.ID, "txtPassword" ).send_keys("admin123")

#driver.find_element_by_id("btnLogin").click()

driver.find_element(By.ID, "btnLogin" ).click()

act_title = driver.title

exp_title = "OrangeHRM"

if (act_title == exp_title):
    print("The Title Test case passed")
else:
    print("The Title test case does not passed")

driver.close()


