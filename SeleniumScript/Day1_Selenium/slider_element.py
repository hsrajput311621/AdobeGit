
import time

import webdriver_manager.utils

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

left_slider = driver.find_element(By.XPATH, "//body//div[2]//div//span[1]")

right_slider = driver.find_element(By.XPATH, "//body//div[2]//div//span[2]")

print("Location of Slider before moving.....")
print(left_slider.location) # {'x': 59, 'y': 251}
print(right_slider.location) # {'x': 613, 'y': 251}

act = ActionChains(driver)

act.drag_and_drop_by_offset(left_slider, 100, 0).perform()
act.drag_and_drop_by_offset(right_slider,-39, 0).perform()

print("Location of Slider after moving.....")
print(left_slider.location) # {'x': 159, 'y': 251}
print(right_slider.location) # {'x': 275, 'y': 251}

time.sleep(3)
driver.close()


