#Open WEb Browser
#Open URL(opensource-demo.orangehrmlive.com)
#Provide Email
#Provide password
#click on login
#Capture title of the dashboard page
#Verify title of teh page
#close browser.
# webdriver is a module and now by importing we can use all the class and the objects.



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.youtube.com")
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://python.org")
time.sleep(2)
driver.close()
driver.quit()
