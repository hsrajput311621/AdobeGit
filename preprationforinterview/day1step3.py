from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\drivers\chromedriver.exe")
driver = webdriver.Chrome(service = serv_obj )
#driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
timeout = 10
driver.maximize_window()
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
mywait = WebDriverWait(driver, timeout, poll_frequency=2,ignored_exceptions=[Exception])
searchlink = mywait.until(EC.presence_of_element_located((By.ID, "login-button")))
searchlink.click()
driver.close()


