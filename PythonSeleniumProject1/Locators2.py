from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/login")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.CLASS_NAME,"forgot-password").click()

driver.find_element(By.ID,"Email").send_keys("hsrajput312116@gmail.com")

driver.close()

serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.gmail.com")



'''
driver.find_element(By.NAME,"send-email").click()


driver.find_element(By.ID,"Email").send_keys("hsrajput312116@gmail.com")

driver.find_element(By.CLASS_NAME, "password").send_keys("admin123")

driver.find_element(By.ID, "RememberMe").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button").click()

#driver.close()

'''