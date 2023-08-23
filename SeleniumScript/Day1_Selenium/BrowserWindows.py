
# Browser windows:
# command use to switch focus to other session or window browser:
# switch_to.window(WindowID)
# How to get the WindowID :
# driver.current_window_handle : Return windowID of a single browser window, they are dynamically generated everytime, it is not same everytime.
#window_handles : return window ID's of multiple browser windows.

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

#windowID = driver.current_window_handle    #CDwindow-646BFFE146DD12A0629F9A145CCA4F9A different when run other time.

#print("The WindowID of the browser is ", windowID)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

windowIDs = driver.window_handles   # it will return multiple browser windowIDS, it is list variable.

# This is first Approach, where we have one, or two browsers and we can perform manual.
parentwindowid = windowIDs[0]
childwindowid = windowIDs[1]
print(parentwindowid, childwindowid)   # CDwindow-FF63C04B5E91680A32BE43C71C4ADB77 CDwindow-DA0DC16FCA4B6C4805163CB07DB0EB6A

time.sleep(2)

driver.switch_to.window(childwindowid)
print("Title of the child window", driver.title)   # OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS

driver.switch_to.window(parentwindowid)
print("The title of the parent window ", driver.title)    # OrangeHRM

#Approach 2 where we need to navigate to more number of browsers in one go, we can use looping statement.

for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)


# If there are more than one browser window and want to close specific browser#

for winid in windowIDs:
    driver.switch_to.window(winid)
    if driver.title =="OrangeHRM":
        driver.close()

time.sleep(2)

driver.quit()

