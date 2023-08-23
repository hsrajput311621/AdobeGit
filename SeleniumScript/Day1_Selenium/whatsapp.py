from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

obj_serv = Service("D:\Web-Driver\chromedriver.exe")

driver = webdriver.Chrome(service=obj_serv)

driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(12)
target = 'Ashi Ji Airtel'
driver.find_element(By.XPATH, "//div[@class='two _1jJ70']").click() # replace target with the name of the contact or group
time.sleep(3)
message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']//p[@class='selectable-text copyable-text iq0m558w']") # locate the message box element
time.sleep(3)
message_box.send_keys('Hello, this is an automated message.') # type the message you want to send
time.sleep(3)
send_button = driver.find_element(By.XPATH, "//span[@data-testid='send']") # locate the send button element
send_button.click() # click the send button
time.sleep(3)
driver.quit() # close the browser window