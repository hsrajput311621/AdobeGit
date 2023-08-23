
# Alerts are those which comes as a popup while working on the web base application.
#Generally we see three types of popup/alerts:
#1) Alert
#2) Confirm, which has two options like : OK and Cancel
#3) Prompt: which has box somthing to srite and OK and Cancel button.

# Auhtentication popup: we need to pass the auth token in the URL:
#Syntax of the adding authentication usernmae and password in url:
# https://admin:admin@the-internet.herokuapp.com/javascript_alerts
# Alert is not a web element we need to use the switch command to switch to
# the alert window, and the alert window need to store in the variable.
# Alerts are the jave script alert.
# we need to use the accept class to close the alert by using OK button
# we need to use the dismiss class to close the alert by using Cancel button.
# When we close the alert by using the cancel button the msg will be null.
# driver.switch_to.alert

import time

import requests as requests

import webdriver_manager.chrome

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(4)

#alertwindow is an object of the alert box.

alertwindow = driver.switch_to.alert   # It is used to switch the focus of the locator to the alert rather than the locator.

print(alertwindow.text)

time.sleep(2)

alertwindow.send_keys("Welcome")  #object is used for alert window is use to enter text in alert box

time.sleep(2)

#alertwindow.accept()     # accept() will click on 'ok' button of alert#

alertwindow.dismiss()    # this will close the alert by cliking cancel button.

time.sleep(3)

driver.close()
