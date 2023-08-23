from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\\Web-Driver\\chromedriver.exe")

driver.get("https://www.google.com/")

driver.maximize_window()

print(driver.title)

print(driver.current_url)

print(driver.application_cache)

print(driver.current_window_handle)

driver.close()