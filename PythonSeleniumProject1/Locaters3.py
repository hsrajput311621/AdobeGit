from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Web-Driver\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

driver.find_element(By.CLASS_NAME,"ico-register").click()

driver.find_element(By.ID,"gender-male").click()

driver.find_element(By.NAME,"FirstName").send_keys("Hitesh")

driver.find_element(By.NAME,"LastName").send_keys("Rajput")
driver.find_element(By.NAME,"DateOfBirthDay").send_keys("30")

driver.find_element(By.NAME, "DateOfBirthMonth").send_keys("October")
driver.find_element(By.NAME, "DateOfBirthYear").send_keys("1991")
driver.find_element(By.ID,"Email").send_keys("hitesh.rajput@gmail.com")
driver.find_element(By.ID,"Password").send_keys("Adobe@2022")

driver.find_element(By.ID,"ConfirmPassword").send_keys("Adobe@2022")
driver.find_element(By.NAME,"register-button").click()

driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[2]/a").click()

driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div/div[4]/div[2]/div[2]/div/div[2]/div[3]/div[2]/button[1]").click()

driver.find_element(By.CLASS_NAME,"button-1").click()

driver.find_element(By.CLASS_NAME,"cart-label").click()

driver.find_element(By.ID, "termsofservice").click()

driver.find_element(By.ID, "checkout").click()


#driver.close()