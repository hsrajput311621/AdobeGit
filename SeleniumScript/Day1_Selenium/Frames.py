# Frames /Iframes
#inner frame

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()  # go back to main page

time.sleep(2)

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content() # go back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
driver.switch_to.default_content() # go back to main page

time.sleep(3)

driver.close()