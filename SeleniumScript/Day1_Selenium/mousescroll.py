
import time

import webdriver_manager.utils

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

#1 Scroll down page by pixel in java script#

# driver.execute_script("window.scrollBy(0,3000)")
# value = driver.execute_script("return window.pageY0ffet:")
# print("Number of pixels", value)

#2 Scroll down page till element is visible:

# flag = driver.find_element(By.XPATH,"//img[@alt = 'Flag of India']" )
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("window.pageY0ffset;")
# print("Number of pixels moved, ", value)

#3 Scroll down the page till end:

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("window.pageY0ffset;")
print("Number of pixels moved, ", value)

#Scroll up to starting position
time.sleep(3)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("window.pageY0ffset;")
print("Number of pixels moved, ", value)

time.sleep(3)

driver.close()

