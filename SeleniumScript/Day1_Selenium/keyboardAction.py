
# In this we will perform the keyboard opetations on the selenium webtool, this will automation the script running in the selenium.

import time

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

act=ActionChains(driver)

text1 = driver.find_element(By.XPATH, "//textarea[@name = 'text1']")

text1.send_keys("Welcome to the Selenium tool")

text2 = driver.find_element(By.XPATH, "//textarea[@name = 'text2']")

# input .....> Ctrl+A select the text

act.key_down(Keys.CONTROL)
act.send_keys("a")

act.key_up(Keys.CONTROL)
act.perform()

#Both the command is same but we can write the above command in single line:

#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1 .....> Ctrl+C Copy text

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

#act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Press tab key to navigate to input2(second)

act.send_keys(Keys.TAB)
act.perform()

#act.send_keys(Keys.TAB).perform()

#PRess CTRL + V ----Paste the text

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

#act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(3)

driver.close()

