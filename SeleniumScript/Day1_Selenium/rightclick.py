

import time

import webdriver_manager.utils

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

button = driver.find_element(By.XPATH, "//span[@class = 'context-menu-one btn btn-neutral']")

act = ActionChains(driver)

act.context_click(button).perform()

driver.find_element(By.XPATH, "//span[normalize-space() = 'Copy']").click()

driver.switch_to.alert.accept()

time.sleep(3)

driver.close()

# driver.close() : Driver command will close the focused window but the driver.
# driver.quit(): driver.quit is internally killing the process from the  background and all the windows in one go, and this will be ask in the interview.
# If we have 5 different windows my requirement is to two or three or four not all, for that we need to capture the ID of the window.
#