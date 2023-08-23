

# Here we are using all the validation regarding the dropdown:

import time

import requests as requests

import webdriver_manager.chrome

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")

driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

dropcountry = driver.find_element(By.XPATH, "//select[@name = 'country_id']")
dropselect = Select(dropcountry)
#dropselect.select_by_visible_text("India")

#dropselect.select_by_value("10")   # Argentina

#dropselect.select_by_index(13) #Australia

# Capture all the options in the dropdown and print them###

alloptions = dropselect.options   # here we are using options for fetching the name of the state in the dropdown.

print("total number of options:", len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# select option from dropdown without using built-in method.
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break

time.sleep(2)

dropvalue = driver.find_elements(By.XPATH, "//*[@id='input-country']/option")

print(len(dropvalue))

for list in dropvalue:
    print(list.text)

driver.close()

# practise from https://testautomationpractice.blogspot.com/
# https://itera-qa.azurewebsites.net/home/automation
