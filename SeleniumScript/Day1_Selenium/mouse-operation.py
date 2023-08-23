
# Action related to mouse in the selenium tool
# Different type of mouse opertion related to selenium
#1) Mouse hover
#2) Double click
#3) Right click


import time

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.XPATH, "//input[@name = 'txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name = 'txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@name = 'Submit']").click()

time.sleep(3)

admin = driver.find_element(By.XPATH,"//b[normalize-space()='Admin']")
usermgmt = driver.find_element(By.XPATH, "//a[@id = 'menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//a[@id = 'menu_admin_viewSystemUsers']")


act=ActionChains(driver)

# This will help to switch hower the mosue with the admin --> Usermanagement ..> users #

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()

time.sleep(3)

driver.close()



