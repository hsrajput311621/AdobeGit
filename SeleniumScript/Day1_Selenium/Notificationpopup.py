# Notification popup#

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()

ops.add_argument("--disable-notifications")

# driver = webdriver.Chrome()

#calling for chrome driver two methods above and the below one
serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver = webdriver.Chrome(service = serv_obj, options=ops)

driver.get("https://whatmylocation.com/")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

time.sleep(2)

driver.close()