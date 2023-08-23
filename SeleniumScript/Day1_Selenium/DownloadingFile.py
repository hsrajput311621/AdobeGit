# The concept of downloading the file is vary browser to browser, firfox is different.


import time

from selenium.webdriver import ActionChains

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def chorme_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\Chromedriver_win32\chromedriver.exe")
    preferences = {"download.default_directory": location} #save file in the desired location
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences) # desired location
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver



#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)