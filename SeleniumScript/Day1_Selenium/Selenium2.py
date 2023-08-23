#Test Case
#1) Open the browser : https://demo.nopcommerce.com/login.
#2) Register with the websie with  personal details
#3) usernmae  = Admin
#4) Password = admin123
#5) capture the title of the website (Actual)
#6) Compare the title with the expected title of the page(Expected).
#7) close the browser.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div/ul/li[1]/a").click()

driver.find_element(By.NAME, "Gender").click()

driver.find_element(By.ID, "FirstName").send_keys("Hitesh")

driver.find_element(By.ID, "LastName").send_keys("Rajput")

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]").send_keys(30)

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]").send_keys("oct")

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]").send_keys(1991)

driver.find_element(By.ID, "Email").send_keys("hsrajput31166")

driver.find_element(By.ID, "Password").send_keys("Adobe@2022")

driver.find_element(By.ID, "ConfirmPassword").send_keys("Adobe@2022")

driver.find_element(By.ID,"register-button").click()

driver.implicitly_wait(5)

driver.close()