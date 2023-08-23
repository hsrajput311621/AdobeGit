
# Links are 3 type we can see in the web pages.

#1) Internal links: we navigate to same page.
#2) Externam links: to navigate to other webpages.
#3) Broker links: those links which do not reach to destination, it is for future implimentation.

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.LINK_TEXT, "Digital downloads").click()

#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

## Find the all the links available in the webpage"

tot_link = driver.find_elements(By.TAG_NAME, "a")

# with the help of XPATH

#driver.find_elements(By.XPATH, "//a")

print(len(tot_link))      # This will find the tolal number of links available in the webppages

# This will pring the name of all the links available in the webpages####

for links in tot_link:
    print(links.text)


# Brokern links: IT is used by the develpoers for future develpments#


time.sleep(2)

driver.close()

