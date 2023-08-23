

#### Wait Commands #####

# time.sleep(time in seconds) : It will hamper the performance of the script, still there is a chance of getting exception
# Implicit wait: It is need to call only one time and we can use it all the program,it always take max time, by the time
# we get the locators the command will execute.
# Explicit wait: it works based on condition, till the locators are visible or present.
#In Explicit we do have the "WebDriverWait" class in the selenium for the Explicit wait, it will take two argument one is object
# and one time in seconds.
# Advantages of the EXplicit wait, in this we do not depend upon the time, and if the locator is not available
# the condition will fail with the cut of time.




import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC   # here EC as a allias of Expected_conditions

driver=webdriver.Chrome()

# syntax for declaration of explicit wait command### and mywait is a object of class, we need to mention this while calling
mywait = WebDriverWait(driver, 10,poll_frequency= 2 , ignored_exceptions=[Exception])
# this is declaration part of the Explicit wait.(class took two variable one is object and one is time.)

driver.get("https:www.google.com/")

# The implicitly wait is a single statment which work for whole script.

driver.implicitly_wait(10)  ##we just need to add the wait at the starting so that we can use the implicit wait at all the position.

driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("selenium")

driver.find_element(By.XPATH, "//input[@title='Search']").submit()

#time.sleep(3)

# here we are adding a function which will wait till the presence of the locator is visible.
#we have use until and EC for initializing the explicit wait command.
searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))

searchlink.click()

# driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

# time.sleep(2)

driver.quit()


