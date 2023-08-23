# difference b/w find_element() and find_elements()
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

print(driver.current_url)

###### find_element() --- Return sigle webelement.............. # find_element() : always return as a web element object not the list element
#1) locator matching with the single webelement

element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("Apple MacBook Pro")

#2) Locator matching with the multiple webelements ....................

links = driver.find_element(By.XPATH, "//div[@class='footer']//a").text

print(links)   #only one single webelement --- Sitemap

#3) Element not available --- It will return exception/error, no such element exception.



############## find_elements() ....... Returns multiple webelement.................  #find_elements(): always return as list elements/collecion, not the web element.

#1)  locator matching with the single webelement
elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")

print(len(elements))    # 1 list

driver.find_element(By.XPATH, "//input[@id='small-searchterms']").clear()

time.sleep(2)

print(elements[0].send_keys("microsoft"))

#2) Locator matching with the multiple webelements

multiple_elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")

print(len(multiple_elements))   # 23

print(multiple_elements[1].text)   # Shipping & returns element at index 1

for ele in multiple_elements:
    print(ele.text)                     # it will print all the link of the fotter page.

#3) Element not available --- it will return zero but not the exception as in find_element()


time.sleep(3)

driver.close()
