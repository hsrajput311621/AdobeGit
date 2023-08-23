# Broken link

# The Broken links are used by developer for further development:

import time

import requests as requests

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

links = driver.find_elements(By.TAG_NAME, "a")

print(len(links))

count=0

for i in range(len(links)):
    print(links[i].text)

for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)     # requests is use to get the broken links of the page, it is a direct method to read/check the links.
    except:
        None

    if res.status_code>=400:
        print(url, "is broken link")
        count+=1
    else:
        print(url, " is valid link")
print("Total number of broken links: ", count)

time.sleep(3)

driver.find_element(By.XPATH, "//a[text() = 'Errorcode 400']").click()

time.sleep(2)

driver.close()