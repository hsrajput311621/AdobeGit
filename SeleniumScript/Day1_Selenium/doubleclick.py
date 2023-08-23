

import time

import webdriver_manager.utils
from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondbiclick3")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.switch_to.frame("iframeResult") # switch to frame for the button#

field1 = driver.find_element(By.XPATH, "//input[@id = 'field1']")
field1.clear()
field1.send_keys("welcome")

button = driver.find_element(By.XPATH, "button[normalize-space()='Copy Text']")

act = ActionChains(driver)

act.double_click(button).perform() # double click action#

 # Drag and Drop by mouse#

act = ActionChains(driver)

Source_ele = driver.find_element(By.ID, "box6")

target_ele = driver.find_element(By.ID, "box106")

act.drag_and_drop(Source_ele, target_ele).perform()  # it will move the source to the destination

