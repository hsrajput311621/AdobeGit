
# In this we are going to use CSS Selectors #

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login/")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

#1(TAG with ID) : Syntax : Tagname#Value of ID

#2(TAG with CLASS): Syntax : Tagname.Value of Class

#3(TAG with ATTRIBUTE): Syntax: tagname[Attribut = value]

#4(TAG, CLASS with ATTRIBUTE): Syntax : tagname.value of Class [ attribute = value ]

driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")

driver.find_element(By.NAME, "email").clear()

driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("xyg@gmail.com")

driver.find_element(By.NAME, "email").clear()

driver.find_element(By.CSS_SELECTOR, "input[autocomplete = username]").send_keys("hitesh@gmail.com")

driver.find_element(By.NAME, "email").clear()

driver.find_element(By.CSS_SELECTOR, "input.inputtext[autocomplete = username]").send_keys("archana@gmail.com")

driver.find_element(By.NAME, "email").clear()

# ----------------- For Password Field-------------------------#

driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("admin")

driver.find_element(By.NAME, "pass").clear()

driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("xygabc")

driver.find_element(By.NAME, "pass").clear()

driver.find_element(By.CSS_SELECTOR, "input[autocomplete = current-password]").send_keys(1234656)

driver.find_element(By.NAME, "pass").clear()

driver.find_element(By.CSS_SELECTOR, "input.inputtext[aria-label = Password]").send_keys("adffasf")

driver.find_element(By.NAME, "pass").clear()

driver.close()