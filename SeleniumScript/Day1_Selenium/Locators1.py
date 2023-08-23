
#Here we can see different types of locators in the Selenium#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")

l = len(sliders)

print("The legth of the sliders or the number of images in the slider is ", l)

links = driver.find_elements(By.TAG_NAME,"a")

count = len(links)

print("The total number of link available in the page is", count)

driver.find_element(By.LINK_TEXT, "Sign in").click()


driver.close()

