#Inner frame

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://demo.automationtesting.in/Frames.html")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outterframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")

driver.switch_to.frame(outterframe)

innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")

driver.switch_to.parent_frame()  #in selenium frame we can switch back to parent frame, from inner frame.

driver.switch_to.default_content() # it will switch back to default/main page.

time.sleep(2)

driver.close()



